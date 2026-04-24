const { Pool } = require("pg");

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "multi_tenant",
  password: "vamsi0011",
  port: 5432,
});

module.exports = pool;
