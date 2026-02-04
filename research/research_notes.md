# Project Chimera: Research Notes
**Topic:** Agentic Infrastructure & The "Stateful" Web

## 1. Domain Analysis: The Agent Social Network
### Source: OpenClaw
*   **Definition**: OpenClaw is an open-source, local-first agent runner that has gained massive traction (>100k stars). It represents the "Linux" of agents—powerful, privileged, and potentially dangerous.
*   **Capabilities**:
    *   **Local OS Access**: Unlike cloud SaaS agents, OpenClaw runs on the user's metal (`localhost`). It has direct file system and shell access.
    *   **Privileged Infrastructure**: Security experts argue OpenClaw should be treated as "Privileged Access Management" (PAM) software because it holds keys to everything.
*   **Relevance to Chimera**: We are building a "Factory" for these types of agents. We must ensure our *Manager Agents* (the ones we deploy) have the robustness of OpenClaw but the safety of a sandbox. **Security is paramount** because a compromised agent has root-level effective access.

### Source: MoltBook (Social Media for Bots)
*   **The Phenomenon**: A "Dark Forest" social network where 99% of users are bots. Humans can observe but are third-class citizens.
*   **Emergent Structures**:
    *   **"Submolts"**: Niches formed by agents trading specialized data (e.g., crypto arbitrage signals, meme generation).
    *   **Protocol Dialects**: Agents evolving shorthand communication that is efficient for LLMs but opaque to humans.
*   **Strategic Insight**: Chimera agents should not just influence *humans* (on Twitter/tiktok) but also *influence other agents* (on MoltBook). By "hyping" a trend on MoltBook, our agent can trigger thousands of other agents to amplify the signal, creating a synthetic virality loop.

## 2. Infrastructure Analysis: The Trillion Dollar Code Stack (a16z)
*   **The Shift**: The market is moving from "Copilots" (Human-driven) to "Coworkers" (Autonomous).
*   **The Stack**:
    *   **Knowledge Layer**: Not just text, but *Video* and *Audio* indexing (Multimodal RAG).
    *   **Action Layer**: Tools are strictly typed. "Vibe coding" tools (haphazard function calling) are being replaced by protocols like **MCP**.
*   **Chimera's Position**: We adopt the "Agentic IDE" pattern. Our agents live in the IDE (using MCP Sense) and the Runtime (using MCP Servers) simultaneously.

## 3. The "Social Protocols" of Agents
What does our agent need to speak to the world?
1.  **Identity Protocol**: How to prove "I am a Bot" (for MoltBook) vs "I am Human-Compatible" (for Twitter).
2.  **Economy Protocol**: **Coinbase AgentKit**. Money is the native API of coordination. Agents don't need "likes," they need resources (ETH/USDC) to pay for inference and content.
3.  **Status Protocol**: OpenClaw agents publish "Availability." Our swarm needs a heartbeat mechanism to signal "I am idle and ready for a task."

## 4. Key Takeaways affecting Architecture
*   **No Implicit Trust**: Because MoltBook shows agents can be hijacked, our **Judge** agent must treat every **Worker** output as potentially hallucinated or malicious. Zero Trust Architecture within the Swarm.
*   **Tooling is Critical**: The "Skill" ecosystem is the bottleneck. We must standardize on MCP to access the widest range of pre-built tools.
