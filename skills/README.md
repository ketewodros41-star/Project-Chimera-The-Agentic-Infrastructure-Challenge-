# Project Chimera: Agent Skills Directory

This directory contains the capability packages used by the Chimera Agent at runtime.

## Skill Structure [FR-2.1]
Each skill must follow the structured contract definition below.

## Critical Skill Contracts

### 1. `skill_download_youtube`
- **Purpose:** Downloads raw video/audio content from YouTube.
- **Input:** `{"url": "string"}`
- **Output:** `{"filepath": "string"}`

### 2. `skill_transcribe_audio`
- **Purpose:** Converts audio content to text transcriptions.
- **Input:** `{"audio_path": "string"}`
- **Output:** `{"transcript": "string"}`

### 3. `skill_generate_caption`
- **Purpose:** Generates engaging captions based on trend data.
- **Input:** `{"trend_data": "dict"}`
- **Output:** `{"caption": "string"}`

## Non-goals
- Manual post approval (handled by HITL Moderator role).
- Direct credential management (handled by Environment Injection).
