# Security & Compliance Framework

Privacy and operational integrity are baked directly into the agent code boundaries.

## Key Management
The symmetric encryption layer (`utils/encryption.py`) expects a 32-byte URL-safe base64 encoded key via the `STORAGE_ENCRYPTION_KEY` environment variable. 

```bash
# Force-generate or rotate a token locally using our administrative tools
python scripts/rotate_keys.py
