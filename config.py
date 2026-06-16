import os
from dotenv import load_dotenv

load_dotenv()

# Network Settings
PORT = int(os.getenv("AGENT_PORT", 8000))
ENDPOINT = os.getenv("AGENT_ENDPOINT", "http://127.0.0.1:8000/submit")
MAILBOX_KEY = os.getenv("ASI_MAILBOX_KEY", None)

# Security Credentials
AGENT_SEED = os.getenv("ASI_AGENT_SEED", "default_fallback_seed_phrase_change_me")

# Retention & Storage Settings
RETENTION_DAYS = 90
RETENTION_TTL_SECONDS = RETENTION_DAYS * 24 * 60 * 60
CLEANUP_INTERVAL_SECONDS = 86400.0  # 24 Hours
