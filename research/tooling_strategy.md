# Project Chimera: Tooling & Skills Strategy

This document outlines the dual-category tooling strategy for both development and runtime operations of the Chimera Agent Swarm.

## Category A: Developer Tools (MCP Infrastructure)

These tools are configured within the IDE to assist the humans and agents during the development phase. They provide standardized access to the repository and operating system.

| Tool | Purpose | Criticality |
|------|---------|-------------|
| **git-mcp** | Programmatic repository management and version control. | 🔴 High |
| **filesystem-mcp** | Secure and standardized file system access. | 🔴 High |
| **Tenx MCP Sense** | The "Flight Recorder." Captures all interaction packets for auditability and debugging. | 🔴 Required |

## Category B: Agent Skills (Runtime Capabilities)

Skills are specific capability packages that the Chimera Agent uses to interact with the world. These are defined in the `skills/` directory.

### 1. Social & Media
- **mcp-server-twitter**: Bi-directional social interactions.
- **mcp-server-youtube**: Video content management.
- **mcp-server-ideogram**: High-fidelity image generation.

### 2. Knowledge & Memory
- **mcp-server-weaviate**: Vector database operations for long-term memory.
- **mcp-server-brave-search**: Real-time web search for trend identification.

### 3. Agentic Commerce
- **mcp-server-coinbase**: Financial operations via Coinbase AgentKit (ETH/USDC transactions).

---
*Note: This strategy ensures that all external interactions are abstracted through the Model Context Protocol (MCP), maintaining traceability and security.*
