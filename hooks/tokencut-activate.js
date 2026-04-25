#!/usr/bin/env node
const fs = require("fs");
const os = require("os");
const path = require("path");
const { getDefaultProfile, safeWriteFlag } = require("./tokencut-config");

const root = path.resolve(__dirname, "..");
const agentsPath = path.join(root, "AGENTS.md");
const skillPath = path.join(root, ".github", "skills", "tokencut", "SKILL.md");
const memorySkillPath = path.join(root, ".github", "skills", "tokencut-memory", "SKILL.md");
const claudeDir = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude");
const flagPath = path.join(claudeDir, ".tokencut-active");

function readSafe(filePath) {
  try {
    return fs.readFileSync(filePath, "utf8");
  } catch {
    return "";
  }
}

const agents = readSafe(agentsPath);
const skill = readSafe(skillPath).replace(/^---[\s\S]*?---\s*/, "");
const memorySkill = readSafe(memorySkillPath).replace(/^---[\s\S]*?---\s*/, "");
const profile = getDefaultProfile();
safeWriteFlag(flagPath, profile);

const output = [
  "TOKENCUT MODE ACTIVE (profile=" + profile + ")",
  "",
  agents.trim(),
  "",
  skill.trim(),
  "",
  memorySkill.trim(),
].filter(Boolean).join("\n");

process.stdout.write(output || "TOKENCUT MODE ACTIVE");
