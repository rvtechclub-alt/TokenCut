# Tokencut Analysis and Tokencut Plan

## 1. Tokencut Strengths

- Multi-agent distribution works: Claude, Codex, Gemini, and skill-based installs.
- Strong prompt-level behavior anchoring through SKILL.md and session activation hooks.
- Practical command ergonomics: level switching and terse helper skills.
- Clear value proposition with measurable token reduction.
- Useful memory compression utility with validation and backup flow.

## 2. Tokencut Weaknesses and Gaps

- Compression style is mostly fixed by mode; weak dynamic adaptation by task intent.
- Rule-heavy behavior can over-compress explanatory contexts.
- Plugin architecture is spread across platform-specific files without a single adapter interface.
- Memory compression relies on external LLM call path and can be expensive/fragile.
- Metrics are benchmarked externally rather than as first-class runtime outputs.
- Partial compression targeting (specific sections) is not a primary user flow.

## 3. TokenCut Rewrite Design

- Keep proven Tokencut mental model but rewrite implementation with modular Python package.
- Add adaptive mode resolver, two-layer compression, and structure-safe placeholder protection.
- Keep command mapping familiar to simplify migration.

## 4. TokenCut Next Design (Fully New)

- Context analyzer drives profile selection and risk-aware compression guards.
- Split compression into semantic and linguistic layers with explainable output map.
- Add partial compression mode for selected markdown sections.
- Add versioned memory snapshots with metadata and digests.
- Add local .tokencutrc runtime control.
- Expose direct benchmark script with normal vs Tokencut-like vs tokencut comparison.

## 5. Deliverables in this workspace

- tokencut-rewrite/: Tokencut-inspired rewrite implementation
- tokencut-next/: fully new Tokencut implementation
- Both include tests and runnable CLI entries

