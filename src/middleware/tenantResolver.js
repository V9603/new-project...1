const pool = require("../db");

module.exports = async function tenantResolver(req, res, next) {
  try {
    const hostHeader = req.headers.host;
    if (!hostHeader) {
      return res.status(400).json({ error: "Missing host header" });
    }

    // Remove port (localhost:3000 → localhost)
    const hostname = hostHeader.split(":")[0];

    // 1. Admin / platform route bypass
    if (
      req.path.startsWith("/admin") ||
      req.path.startsWith("/platform")
    ) {
      req.tenant = null;
      return next();
    }

    // 2. Extract subdomain
    const parts = hostname.split(".");
    let subdomain = null;

    // Local development (abc.localhost)
    if (hostname.includes("localhost")) {
      if (parts.length > 1) {
        subdomain = parts[0];
      }
    } else {
      // Production domains (abc.platform.com)
      if (parts.length > 2) {
        subdomain = parts[0];
      }
    }

    // 3. Resolve tenant using subdomain OR custom domain
    const query = `
      SELECT * FROM tenants
      WHERE (subdomain = $1 OR custom_domain = $2)
      AND is_active = true
      LIMIT 1
    `;

    const result = await pool.query(query, [subdomain, hostname]);

    // 4. Reject unknown or inactive tenants
    if (result.rows.length === 0) {
      return res.status(404).json({
        error: "Tenant not found or inactive",
      });
    }

    // 5. Attach tenant context to request
    req.tenant = result.rows[0];

    next();
  } catch (error) {
    console.error("Tenant resolution error:", error);
    res.status(500).json({
      error: "Tenant resolution failed",
    });
  }
};
