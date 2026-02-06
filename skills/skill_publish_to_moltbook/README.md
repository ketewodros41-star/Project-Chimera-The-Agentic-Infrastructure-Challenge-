# Skill: skill_publish_to_moltbook

## Purpose
The final stage interaction tool for publishing synthetic content to the MoltBook agent network.

## Interface Contract (JSON)

### Inputs
```json
{
  "payload": "json",
  "submolt": "string",
  "priority": "bool"
}
```

### Outputs
```json
{
  "post_id": "string",
  "status": "success | failure",
  "timestamp": "iso8601"
}
```

## Failure Modes
- `SUBMOLT_REJECTION`: The target submolt has blacklisted the agent.
- `RATE_LIMIT`: Too many posts in a given timeframe.
- `PAYLOAD_INVALID`: The content does not match MoltBook protocol requirements.
