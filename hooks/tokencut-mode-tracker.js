#!/usr/bin/env node
const fs = require("fs");
const os = require("os");
const path = require("path");
const { getDefaultProfile, safeWriteFlag, readFlag } = require("./tokencut-config");

const claudeDir = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude");
const flagPath = path.join(claudeDir, ".tokencut-active");

let input = "";
process.stdin.on("data", (chunk) => {
  input += chunk;
});

process.stdin.on("end", () => {
  try {
    const data = JSON.parse(input || "{}");
    const prompt = String(data.prompt || "").trim().toLowerCase();

    if (prompt.startsWith("/tokencut")) {
      const parts = prompt.split(/\s+/);
      const cmd = parts[1] || "";

      if (cmd === "off") {
        try {
          fs.unlinkSync(flagPath);
        } catch {}
      } else if (cmd === "auto" || cmd === "dev" || cmd === "learn" || cmd === "fast") {
        safeWriteFlag(flagPath, cmd);
      } else if (cmd === "on" || cmd === "") {
        safeWriteFlag(flagPath, getDefaultProfile());
      }
    }

    if (/\b(tokencut)\b/.test(prompt) && /\b(stop|disable|off|normal)\b/.test(prompt)) {
      try {
        fs.unlinkSync(flagPath);
      } catch {}
    }

    const active = readFlag(flagPath);
    if (active && active !== "off") {
      process.stdout.write(JSON.stringify({
        hookSpecificOutput: {
          hookEventName: "UserPromptSubmit",
          additionalContext:
            "TOKENCUT ACTIVE (profile=" + active + "). Keep responses dense and accurate. Preserve code/JSON/markdown structure."
        }
      }));
    }
  } catch {
    // Silent fail.
  }
});
