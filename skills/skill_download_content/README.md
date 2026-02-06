# Skill: skill_download_content

## Purpose
Fetches raw media from external social protocols and repositories.

## Interface Contract (JSON)

### Inputs
```json
{
  "url": "string",
  "provider": "string (e.g., youtube, twitter, s3)",
  "auth_token": "string (optional)"
}
```

### Outputs
```json
{
  "local_path": "string",
  "bytes": "int",
  "mime_type": "string",
  "checksum": "string"
}
```

## Failure Modes
- `INVALID_URL`: The provided URL is unreachable or malformed.
- `PROVIDER_UNAVAILABLE`: The target social platform is down.
- `INSUFFICIENT_STORAGE`: Local disk space is exhausted.
- `AUTH_FAILED`: Invalid credentials for protected content.

## Non-goals
- Browser automation (stateless HTTP fetch only).
- Dynamic decryption of encrypted media.
- Large-scale data transformation (stateless download only).
