#!/usr/bin/env node
const fs = require("fs");

const VALID_PROFILES = new Set(["auto", "dev", "learn", "fast", "off"]);

function safeWriteFlag(filePath, value) {
  if (!VALID_PROFILES.has(value)) {
    return;
  }
  try {
    fs.writeFileSync(filePath, value, { encoding: "utf8" });
  } catch {
    // Silent by design.
  }
}

function readFlag(filePath) {
  try {
    const raw = fs.readFileSync(filePath, "utf8").trim().toLowerCase();
    if (!VALID_PROFILES.has(raw)) {
      return null;
    }
    return raw;
  } catch {
    return null;
  }
}

function getDefaultProfile() {
  const fromEnv = (process.env.TOKENCUT_DEFAULT_PROFILE || "auto").toLowerCase();
  if (!VALID_PROFILES.has(fromEnv) || fromEnv === "off") {
    return "auto";
  }
  return fromEnv;
}

module.exports = {
  VALID_PROFILES,
  safeWriteFlag,
  readFlag,
  getDefaultProfile,
};
