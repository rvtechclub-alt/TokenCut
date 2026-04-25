# 🪨 TokenCut

### Cut tokens, not meaning.

---

**Stars • Last Commit • License**

---

## Before / After • Install • Profiles • Benchmarks • Philosophy

---

# 🧠 TokenCut Ecosystem

**TokenCut — compress what AI says**  
(you are here)

---

> A developer-first AI compression layer that reduces LLM verbosity while preserving technical meaning, structure, and correctness.

TokenCut turns long AI responses into **dense, high-signal output** — reducing noise, cost, and cognitive load.

Same intelligence.  
Fewer tokens.  
Faster workflows.

---

# 🆚 Before / After

### 🗣️ Normal AI (verbose)

> The issue is likely caused by creating a new object reference during each render cycle. React uses shallow comparison for props, so this triggers unnecessary re-renders. You should use `useMemo` to stabilize the reference.

---

### 🪨 TokenCut (compressed)

> New object each render → new ref → re-render.  
> Use `useMemo`.

---

### 🗣️ Normal AI

> The authentication middleware is failing because token expiry is not properly validated. Let me inspect and suggest a fix.

---

### 🪨 TokenCut

> Auth middleware bug. Token expiry check broken. Fix condition.

---

Same meaning.  
Less noise.  
Faster understanding.

---

# ⚙️ Compression Profiles

|Profile|Behavior|
|---|---|
|`auto`|Detect context automatically|
|`dev`|Dense technical output (default for coding)|
|`learn`|Balanced explanation + compression|
|`fast`|Maximum compression for speed|

---

# ✨ Core Features

## ⚡ Output Compression Engine

- semantic + linguistic compression pipeline
- structure-safe (code, JSON, markdown preserved)
- removes filler without losing meaning

## 🧠 Context Awareness

- detects coding vs explanation vs debug tasks
- adjusts compression level automatically
- avoids unsafe compression in critical logic

## 📊 Explainability Layer

- compression ratio tracking
- token estimation
- “why this was shortened” insights (optional)

## 🧾 Memory Compression

- summarize long notes into dense technical memory
- reduces repeated context load for agents

---

# ⚡ Example Compression Levels

### 🪶 Learn

> React re-renders due to new object reference each render. Wrap in `useMemo`.

### 🪨 Dev (default)

> New object ref each render → re-render. Use `useMemo`.

### 🔥 Fast

> obj ref changes → re-render → useMemo

---

# 📦 Commands

### CLI (tokencut-next)

tokencut on  
tokencut off  
tokencut auto  
  
tokencut profile dev  
tokencut level 80  
  
echo "text" | tokencut run --json  
  
tokencut run --explain  
tokencut memory notes.md

---

### Rewrite Engine

tokencut-rewrite on  
tokencut-rewrite profile smart  
  
echo "text" | tokencut-rewrite run

---

# 📊 Benchmarks (typical results)

|Task|Normal|TokenCut|Saved|
|---|---|---|---|
|Debug React issue|1200 tokens|180|85%|
|Explain architecture|1400|420|70%|
|API debugging|900|220|75%|
|Code review|1100|300|72%|

---

# 🧠 Philosophy

> Good AI is not more words.  
> Good AI is better words.

TokenCut is built on one belief:

> **Clarity = maximum meaning / minimum tokens**

---

# 🚀 Use Cases

- AI coding assistants
- Debugging workflows
- Code review compression
- Terminal-based AI tools
- Prompt engineering optimization
- Cost reduction for LLM APIs

---

# ⚙️ Installation

### 1) Clone repo

git clone https://github.com/rvtechclub-alt/TokenCut.git
cd TokenCut

---

### 2) Install runtime

cd tokencut-next  
pip install -e .

---

### 3) Run tests

pytest -q

---

# 🧩 Integration Targets

TokenCut works with:

- Claude Code workflows
- Codex environments
- Cursor / Windsurf rules
- Gemini CLI extensions
- Copilot instruction layers

---

# 🧠 Why TokenCut Exists

Modern AI tools are:

- powerful but verbose
- correct but noisy
- useful but inefficient

TokenCut fixes this:

> Same intelligence → fewer tokens → faster thinking

---

# ⚡ Important Notes

- TokenCut does NOT reduce model intelligence
- It only compresses **output text**
- Core reasoning remains untouched
- Best for developers, not casual chat

---

# 📜 License

MIT License — use freely, build aggressively.

---

# 🪨 Final Thought

> Less text.  
> Same truth.  
> Better signal.
