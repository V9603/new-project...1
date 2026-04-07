const express = require("express");
const connectDB = require("./src/config/db");
const authRoutes = require("./src/routes/authRoutes");
const adminRoutes = require("./src/routes/adminRoutes"); // <-- add this
const rateLimit = require("express-rate-limit");

require("dotenv").config();

const app = express();
app.use(express.json());
connectDB();

// Rate limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10,
  message: { message: "Too many requests, try again later" },
});

app.use("/api/auth/login", authLimiter);
app.use("/api/auth/forgot-password", authLimiter);

// Routes
app.use("/api/auth", authRoutes);
app.use("/api/admin", adminRoutes); // <-- add this

app.get("/", (req, res) => res.send("API Running..."));

app.listen(5000, () => console.log("Server running on port 5000"));
