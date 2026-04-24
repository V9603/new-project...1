const express = require("express");
const tenantResolver = require("./middleware/tenantResolver");

const app = express();

app.use(express.json());
app.use(tenantResolver);

app.get("/", (req, res) => {
  res.json({
    message: "Server working",
    tenant: req.tenant
  });
});

app.get("/admin", (req, res) => {
  res.json({
    message: "Platform admin route",
    tenant: req.tenant
  });
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
