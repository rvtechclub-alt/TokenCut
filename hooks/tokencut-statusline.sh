#!/usr/bin/env bash
claude_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
flag="$claude_dir/.tokencut-active"

if [ -f "$flag" ]; then
  mode="$(cat "$flag" 2>/dev/null | tr '[:upper:]' '[:lower:]')"
  if [ -z "$mode" ] || [ "$mode" = "auto" ]; then
    printf "[TOKENCUT]"
  else
    up_mode="$(echo "$mode" | tr '[:lower:]' '[:upper:]')"
    printf "[TOKENCUT:%s]" "$up_mode"
  fi
fi
