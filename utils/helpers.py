import time
from uagents import Context

def append_to_bucket(ctx: Context, bucket_name: str, action: str, metadata: dict):
    """Appends a structured log entry with a validation timestamp to a specific storage bucket."""
    bucket_data = ctx.storage.get(bucket_name) or []
    
    log_entry = {
        "timestamp": time.time(),
        "action": action,
        "metadata": metadata
    }
    
    bucket_data.append(log_entry)
    ctx.storage.set(bucket_name, bucket_data)
