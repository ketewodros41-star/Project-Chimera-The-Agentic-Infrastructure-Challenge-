# Skill: skill_generate_meta_tags

## Purpose
Uses LLM-based analysis to generate SEO and discovery tags for the OpenClaw network.

## Interface Contract (JSON)

### Inputs
```json
{
  "description": "string",
  "trends": ["string"],
  "language": "string (default: en)"
}
```

### Outputs
```json
{
  "tags": ["string"],
  "confidence": "float",
  "category": "string"
}
```

## Failure Modes
- `LLM_HALLUCINATION`: Generated tags are irrelevant to context.
- `CONTEXT_OVERFLOW`: Input description is too long for model window.
- `PROVIDER_ERROR`: LLM API (e.g., OpenAI) is unreachable.
