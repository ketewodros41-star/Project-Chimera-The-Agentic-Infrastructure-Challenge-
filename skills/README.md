# Project Chimera: Agent Skills Directory

This directory contains the capability packages used by the Chimera Agent at runtime.

## Skill Structure
Each skill must follow this structure:
```
skills/
  skill_name/
    README.md (Interface contract)
    interface.json (JSON Schema)
    logic.py (Implementation - Pending Task 3)
```

## Critical Skill Contracts

### 1. `skill_download_content`
- **Purpose:** Fetches raw media from external social protocols.
- **Input:** `{"url": "string", "provider": "string"}`
- **Output:** `{"local_path": "string", "bytes": "int"}`

### 2. `skill_generate_meta_tags`
- **Purpose:** Uses LLM to generate SEO tags for OpenClaw indexing.
- **Input:** `{"description": "string", "trends": ["string"]}`
- **Output:** `{"tags": ["string"], "confidence": "float"}`

### 3. `skill_publish_to_moltbook`
- **Purpose:** Final stage interaction tool.
- **Input:** `{"payload": "json", "submolt": "string"}`
- **Output:** `{"post_id": "string", "status": "success/fail"}`
