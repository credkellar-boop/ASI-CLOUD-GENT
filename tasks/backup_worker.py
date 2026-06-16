import json
import os
from datetime import datetime
from uagents import Context

BACKUP_DIR = "./storage_data/backups"

def export_storage_archive(ctx: Context, bucket_name: str) -> str:
    """Serializes and archives a targeted data bucket before permanent deletion."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    records = ctx.storage.get(bucket_name) or []
    if not records:
        return "EMPTY_BUCKET"
        
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"{BACKUP_DIR}/{bucket_name}_archive_{timestamp}.json"
    
    with open(filename, "w") as backup_file:
        json.dump(records, backup_file, indent=4)
        
    ctx.logger.info(f"💾 Secure cold-storage file written successfully: {filename}")
    return filename
