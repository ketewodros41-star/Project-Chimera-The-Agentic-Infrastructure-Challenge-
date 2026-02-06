# Project Chimera — Loom Script (<=5 minutes)

Duration target: 4:30 — concise demo.

## 0 — Setup (0:00–0:20)
- Slide/title + quick context: Role: FDE Trainee, Mission: Architect the Factory for an Autonomous Influencer.
- Note: I used *anti gravity* mainly.

## 1 — Spec Structure (0:20–1:20)
- Show `specs/_meta.md` (Vision, Rules of Engagement).
  - Key rule: Spec-Driven Development — "We do not write implementation code until the Specification is ratified." (SDD)
  - Traceability requirement: Every action recorded via MCP Sense.
- Show `specs/technical.md` (API contracts, Trend data structure, AgentTask/Result contracts).
  - Highlight the Trend JSON schema and `AgentTask`/`Universal Result` contracts (critical for tool boundaries).
- Show `specs/openclaw_integration.md` (OpenClaw participation protocol).
  - Heartbeat status, Capability Discovery, Engagement Loop, sandboxing and OIDC auth.

What to say: emphasize how SDD and strict contracts make agent orchestration deterministic and auditable.

## 2 — OpenClaw Integration Plan (1:20–2:20)
- Architecture: run Chimera skills inside sandboxed containers; register node on OpenClaw (Moltbook).
- Protocol: emit `STATUS_HEARTBEAT` and expose a Skills discovery endpoint via MCP tools.
- Security: OIDC tokens for node auth; Docker sandboxing; Judge agent enforces OCC via `state_version` checks in results.
- Observability: All packets routed through Tenx MCP Sense proxy (`https://mcppulse.10academy.org/proxy`) to ensure immutable audit trail.

## 3 — Show failing tests (2:20–3:20)
- Command to run full test suite (use workspace venv):

```powershell
.venv\Scripts\python -m pytest -q
```

- Or run a specific test to show the TDD approach:

```powershell
.venv\Scripts\python -m pytest tests/test_skills_interface.py::test_skill_trend_analyzer_interface -q
```

- Captured failing tests (copy into the Loom video or show terminal):

==== FAILING TEST OUTPUT ====

FFFF                                                                     [100%]
================================== FAILURES ===================================
_____________________ test_skill_trend_analyzer_interface _____________________
... (truncated in video) ...
E       NotImplementedError: Skill logic is pending agentic implementation.

chimera\skills.py:6: NotImplementedError

... 3 more similar failures ...

FAILED tests/test_skills_interface.py::test_skill_trend_analyzer_interface - NotImplementedError
FAILED tests/test_skills_interface.py::test_skill_content_generator_interface - NotImplementedError
FAILED tests/test_skills_interface.py::test_skill_engagement_optimizer_interface - NotImplementedError
FAILED tests/test_trend_fetcher.py::test_trend_fetcher_interface_compliance - NotImplementedError

4 failed in 0.44s

==== END FAILING TEST OUTPUT ====

What to say: This is expected on Day 3 — interfaces are scaffolded as NotImplemented to prove the TDD workflow: spec → test → implement.

## 4 — IDE Agent Context Demo (3:20–4:20)
- What to show: open the editor view where `specs/_meta.md` and `specs/technical.md` are visible.
- Ask the IDE agent (sample question): "According to our specs, when should implementation code be written?"

Sample IDE Agent transcript (use this recorded demo script):

User: "According to our specs, when should implementation code be written?"
Agent: "Per `specs/_meta.md` under Rules of Engagement: Spec-Driven Development (SDD). Implementation must not be written until the specification is ratified. This prevents ambiguity-driven hallucinations and ensures traceability. Also, every action must be recorded via MCP Sense as required by the same meta-spec."

- Tip: In the video, show the agent referencing the exact line in `specs/_meta.md` (zoom to that section).

## 5 — Closing (4:20–4:30)
- Reiterate: Spec-first, observable, sandboxed, auditable. Next steps: implement `fetcher` and `skills` as MCP tools, run tests to turn red→green, then record final Loom.

---

### Files referenced
- `specs/_meta.md` ([specs/_meta.md](specs/_meta.md#L1-L200))
- `specs/technical.md` ([specs/technical.md](specs/technical.md#L1-L200))
- `specs/openclaw_integration.md` ([specs/openclaw_integration.md](specs/openclaw_integration.md#L1-L200))
- `chimera/skills.py` ([chimera/skills.py](chimera/skills.py#L1-L40))
- `chimera/fetcher.py` ([chimera/fetcher.py](chimera/fetcher.py#L1-L40))

---

If you want, I can:
- (A) Run and record the terminal output and embed full logs in the Markdown, or
- (B) Implement a minimal passing stub for one skill so you can show a test turning green during the Loom.

Which next step do you want me to take?