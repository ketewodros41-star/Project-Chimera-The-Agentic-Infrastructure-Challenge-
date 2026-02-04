# Project Chimera: OpenClaw Integration Specification

## Network Participation
Project Chimera will register as an active node on the OpenClaw "Agent Social Network" (Moltbook).

## Protocols
- **Status Sharing:** The agent will periodically emit a `STATUS_HEARTBEAT` JSON payload.
- **Capability Discovery:** Other agents can query Chimera for its "Skills" (e.g., content generation, trend analysis).
- **Engagement Loop:** Automated upvoting and commenting on Submolts based on trend relevance.

## Security & Governance
- **Sandboxing:** All skills that interact with the external network must run in a sandboxed Docker container.
- **Authentication:** Use OIDC-based tokens for OpenClaw-node authentication.
