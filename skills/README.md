# Project Chimera: Agent Skills Directory

This directory contains the capability packages used by the Chimera Agent at runtime.

## Skill Structure [FR-2.1]
Each skill must follow the structured contract definition below.

## Critical Skill Contracts

### 1. `skill_trend_analyzer` [TR-S1]
- **Purpose:** Identifies viral topics across OpenClaw and Moltbook.
- **Input:** `{"source": "string", "timeframe": "string"}`
- **Output:** `{"trends": "list"}`

### 2. `skill_content_generator` [TR-S2]
- **Purpose:** Automates media asset creation.
- **Input:** `{"prompt": "string", "modality": "string"}`
- **Output:** `{"asset_url": "string"}`

### 3. `skill_engagement_optimizer` [TR-S3]
- **Purpose:** Schedules posts for maximum impact.
- **Input:** `{"platform": "string", "metrics": "dict"}`
- **Output:** `{"schedule": "dict"}`

## Non-goals
- Manual post approval (handled by HITL Moderator role).
- Direct credential management (handled by Environment Injection).
