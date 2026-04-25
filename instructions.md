You are an expert software engineer, LLM systems designer, and developer tooling specialist.

Your task is to deeply analyze the GitHub repository:
tokencut-project/tokencut

Then design and implement a significantly improved version called **TokenCut**.

---

## ðŸŽ¯ Objective

Build a next-generation AI compression layer that:

* Reduces LLM verbosity more intelligently than Tokencut
* Preserves or improves clarity and correctness
* Adds adaptive, context-aware compression
* Improves developer usability and extensibility

---

## ðŸ” Step 1: Analyze Existing Repo (Tokencut)

Thoroughly analyze:

* Architecture and folder structure
* Plugin system (Claude, Codex, Gemini integrations)
* Command handling (/Tokencut, modes, hooks)
* Compression approach (rule-based vs prompt-based)
* Tokencut-compress logic for input compression
* Auto-activation system and hooks
* Skills (commit, review, help)

### Identify:

* Strengths (why it works well)
* Weaknesses (limitations, edge cases)
* Missing features
* Scalability issues
* UX problems

---

## ðŸ§  Step 2: Design TokenCut (Improved Version)

Design TokenCut as a modular, extensible system.

### Core Improvements Required:

#### 1. Adaptive Compression Engine

* Dynamically adjust compression level based on:

  * Task type (debugging, explanation, code, chat)
  * User intent
  * Complexity of response
* Avoid over-compression when clarity is needed

---

#### 2. Context-Aware Modes

Instead of fixed modes, implement:

* Smart mode (auto-detect verbosity level)
* Developer mode (aggressive compression)
* Learning mode (balanced explanation + brevity)

---

#### 3. Structured Output Support

* Preserve formatting:

  * Code blocks
  * JSON
  * Markdown
* Ensure no loss of structure

---

#### 4. Two-Layer Compression

* Layer 1: Semantic compression (remove redundancy)
* Layer 2: Linguistic compression (shorten phrasing)

---

#### 5. Plugin Architecture

* Clean abstraction for:

  * Claude
  * Codex
  * Gemini
  * Future agents
* Make adding new agents easy

---

#### 6. Command System

Design improved commands:

* /tokencut on|off
* /tokencut auto
* /tokencut level <0â€“100>
* /tokencut profile <dev|learn|fast>

---

#### 7. Memory Compression (Better than Tokencut-compress)

* Intelligent summarization instead of just shortening
* Preserve important context
* Versioned memory files

---

#### 8. Metrics & Feedback

* Show:

  * Tokens saved
  * Compression ratio
  * Response time improvement

---

## ðŸ—ï¸ Step 3: Implementation Requirements

* Use clean, modular architecture
* Language: (choose Node.js or Python)
* Separate:

  * Core compression engine
  * Agent adapters
  * CLI interface

### Suggested Structure:

```
tokencut/
  core/
    compressor.ts
    modes.ts
    analyzer.ts
  adapters/
    claude.ts
    codex.ts
    gemini.ts
  commands/
    cli.ts
  utils/
  tests/
```

---

## ðŸ§ª Step 4: Benchmarking

Recreate Tokencut-style benchmarks:

* Compare:

  * Normal output
  * Tokencut output
  * TokenCut output

Measure:

* Token count
* Clarity score (heuristic)
* Compression %

---

## âœ¨ Step 5: Enhancements Beyond Tokencut

Add features Tokencut does NOT have:

* Context-aware compression (major differentiator)
* Partial compression (only certain sections)
* Explain mode toggle (expand compressed output)
* IDE integration hooks
* Config file (.tokencutrc)

---

## ðŸš« Constraints

* Do NOT just copy Tokencut
* Reuse ideas, but rewrite logic and architecture
* Improve naming, structure, and extensibility
* Ensure production-quality code

---

## ðŸ“¦ Final Deliverables

1. Full TokenCut codebase
2. Clean README.md
3. Example usage
4. Benchmarks vs Tokencut
5. Modular plugin system

---

## ðŸ§  Guiding Principle

â€œMaximize information density without sacrificing understanding.â€

---

Now begin:

* First output: analysis of Tokencut repo
* Then: TokenCut architecture design
* Then: implementation
* Then: benchmarks

