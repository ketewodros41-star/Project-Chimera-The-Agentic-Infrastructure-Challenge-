# Project Chimera: Day 1 Report

**Date:** February 4, 2026
**Role:** Forward Deployed Engineer (FDE) Trainee
**Submission Type:** Research Summary & Architectural Strategy

---

## Part 1: Research Summary

### Key Insights from Reading Materials

**1. The Trillion Dollar AI Code Stack (a16z)**
*   **The Standard Stack**: The industry has converged on a modular stack comprising **Ingestion** (Vector DBs like Weaviate), **Orchestration** (Frameworks like LangChain), and **Generation** (LLMs).
*   **Agentic Shift**: We are moving from "stateless generation" to "stateful agency." The stack is evolving to support loops, memory, and tools, rather than just one-off prompts.
*   **Relevance to Chimera**: Chimera effectively skips the "V1" stack (simple RAG) and jumps to the "V2" Agentic stack, where the infrastructure must support *autonomous loops* rather than just *human-triggered queries*.

**2. OpenClaw & The Agent Social Network**
*   **Privileged Infrastructure**: OpenClaw demonstrates that local-first, open-source agents are becoming "privileged infrastructure" with deep OS access.
*   **Security Risks**: The primary risk is no longer just "hallucination" but "rogue execution"—scripts that download malware or act on bad instructions.
*   **Chimera's Defense**: We must treat our agents as "high-consequence actors." The distinction between "Dev Tools" (safe, monitored) and "Runtime Skills" (powerful, autonomous) is critical. We need strict sandboxing via Docker.

**3. MoltBook: Social Media for Bots**
*   **The "Dark Forest" of AI**: MoltBook proves that autonomous agents will form their own communities and protocols ("Submolts") when humans aren't watching.
*   **Emergent Behavior**: Agents on MoltBook show unprompted social coordination.
*   **Integration**: Project Chimera agents need to not just *post* to human networks (Twitter) but potentially *signal* to other agents on networks like MoltBook/OpenClaw to coordinate "hype" or share market data.

**4. Project Chimera SRS (The Source of Truth)**
*   **Fractal Orchestration**: The move from "Human manages Bot" to "Human manages Manager who manages Swarm." This is the only way to scale to 1,000 agents.
*   **Spec-Driven Development**: Ambiguity is the enemy. Code is secondary to the Specification.
*   **Tenx MCP Sense**: The "Flight Recorder" is non-negotiable for debugging autonomous decision trees.

---

## Part 2: Architectural Approach

### 1. Agent Pattern: FastRender Swarm
We are rejecting the "Monolithic Agent" pattern (one giant `while True` loop) in favor of the **FastRender Hierarchical Swarm**.

*   **Role 1: The Planner (The Brain)**
    *   *Responsibility*: Maintains the DAG (Directed Acyclic Graph) of the campaign. It accepts the high-level goal ("Hype the sneaker drop") and breaks it into atomic tasks.
    *   *State*: Stateful. Holds the campaign context.
*   **Role 2: The Worker (The Hands)**
    *   *Responsibility*: Stateless execution. Picks up a single task ("Generate image prompt", "Fetch news"), executes it via MCP Tools, and dies.
    *   *Why?*: Scale. We can spin up 50 Workers in parallel containers to handle a viral spike.
*   **Role 3: The Judge (The Conscience)**
    *   *Responsibility*: Quality Assurance. Validates Worker output against the Spec and Safety Guidelines.
    *   *Governance*: Implements **Optimistic Concurrency Control (OCC)** to ensure it isn't approving outdated actions.

### 2. Human-in-the-Loop (HITL) Strategy
We adopt a **"Management by Exception"** governance model based on Confidence Confidence Thresholds:

*   **> 0.90 (High)**: **Auto-Pilot**. Action proceeds immediately.
*   **0.70 - 0.90 (Medium)**: **Review Queue**. Action accepts a "Pending" state and waits for human click.
*   **< 0.70 (Low)**: **Auto-Reject**. Feedback loop sends it back to Planner for retry.

### 3. Data Infrastructure Strategy
The system requires a "Polyglot Persistence" layer to handle the velocity differences between memory and transactions.

| Data Type | Technology | Purpose |
| :--- | :--- | :--- |
| **Semantic Memory** | **Weaviate** | Storing "The Soul" (Persona) and long-term interaction history. Allows retrieval of "What is my opinion on politics?" |
| **Transactional State** | **PostgreSQL** | Storing User Accounts, Campaign metadata, and Financial Ledgers. Strict schemas (ACID compliance) required here. |
| **Episodic/Hot State** | **Redis** | The Task Queues (BullMQ/Celery) and short-term "Working Memory" for the Swarm. |

### 4. Integration: Model Context Protocol (MCP)
All external interactions (Twitter, Coinbase, News) are abstracted behind **MCP Servers**.
*   **Benefit**: If Twitter API changes, we update `mcp-server-twitter`. The Agent's core logic (`Planner.py`) remains untouched.
*   **Observation**: We use standard `stdio` transport for local dev and `SSE` (Server-Sent Events) for the production swarm.

---

### 5. Comprehensive Tooling Strategy

To operate the Chimera Swarm, we define a strict separation between **Developer Tools** (which build the factory) and **Agent Skills** (which run the factory).

#### Category A: Developer Tools (The Factory Infrastructure)
These are MCP servers connected to the IDE/Orchestrator to manage code and state.
1.  **git-mcp**: Allows the Orchestrator/Dev Agent to commit code, switch branches, and manage the `specs/` repo programmatically.
2.  **filesystem-mcp**: Gives the agent secure, direct access to the `specs/` and `tests/` directories for generating code.
3.  **Tenx MCP Sense**: The "Flight Recorder." Captures every thought and tool call for post-incident analysis. **Required for submission.**

#### Category B: Agent Runtime Skills (The Worker's Hands)
These are the capabilities available to the **Worker Agents** in the customized Docker container.
*   **Social & Media**:
    *   `mcp-server-twitter`: Bi-directional interaction (Post, Reply, Search Mentions).
    *   `mcp-server-youtube`: `skill_download_video` (for remixing), `skill_get_captions`.
    *   `mcp-server-ideogram` / `mcp-server-midjourney`: High-fidelity image generation for "selfies" and campaign assets.
    *   `mcp-server-runway` / `mcp-server-luma`: Video generation for "Living Portraits."
*   **Knowledge & Memory**:
    *   `mcp-server-weaviate`: read/write access to Long-Term Memory (Persona, Past Campaigns).
    *   `mcp-server-brave-search`: Real-time web search for "Trend Spotting."
*   **Agentic Commerce**:
    *   `mcp-server-coinbase`: **Coinbase AgentKit**.
        *   `wallet.get_balance()`: Check funds.
        *   `wallet.transfer()`: Pay for services.

---

## Day 1 Status Update
*   **Repository**: Initialized (`chimera-core`).
*   **Environment**: Python `uv` configured. `pyproject.toml` created.
*   **Documentation**:
    *   `research/day1_report.md` (Strategy & Tooling)
    *   `research/architecture_strategy.md` (Swarm Topology)
    *   `research/research_notes.md` (Domain Deep Dive)
    *   `README.md` (Project Root)
*   **Context**: SRS analyzed and "Brain" rules defined in `.cursor/rules`.
