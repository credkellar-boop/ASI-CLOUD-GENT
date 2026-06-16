import time
from uagents import Agent, Context, Model

# --- Configuration & Time constants ---
# 90 Days = 90 days * 24 hours * 60 minutes * 60 seconds
RETENTION_TTL_SECONDS = 90 * 24 * 60 * 60 
CLEANUP_INTERVAL_SECONDS = 86400.0  # Check for garbage once every 24 hours

class NetworkMessage(Model):
    payload: str

# Initialize the storage-centric agent
storage_agent = Agent(
    name="secure_storage_agent", 
    seed="isolated_storage_cluster_seed_phrase",
    port=8002,
    endpoint=["http://127.0.0.1:8002/submit"]
)

# --- 1. Storage Structure Initialization ---
@storage_agent.on_event("startup")
async def initialize_buckets(ctx: Context):
    """Initializes separate structured partitions inside the agent's memory."""
    buckets = ["sent_info", "received_info", "user_import_logs", "action_logs"]
    
    for bucket in buckets:
        if not ctx.storage.get(bucket):
            ctx.storage.set(bucket, [])
            
    ctx.logger.info("✅ All recommended storage partitions initialized securely.")

# --- 2. Centralized Log Insertion Engine ---
def append_to_storage_bucket(ctx: Context, bucket_name: str, action: str, metadata: dict):
    """Helper method to log data packets alongside an absolute unix timestamp."""
    bucket_data = ctx.storage.get(bucket_name) or []
    
    log_entry = {
        "timestamp": time.time(),
        "action": action,
        "metadata": metadata
    }
    
    bucket_data.append(log_entry)
    ctx.storage.set(bucket_name, bucket_data)

# --- 3. Example Use Cases (Tracking Activity) ---
@storage_agent.on_message(model=NetworkMessage)
async def handle_incoming_message(ctx: Context, sender: str, msg: NetworkMessage):
    """Example of logging data when receiving information."""
    ctx.logger.info(f"Processing message from {sender}")
    
    # Log the action to 'received_info' bucket
    append_to_storage_bucket(
        ctx=ctx,
        bucket_name="received_info",
        action="DATA_RECEIVED",
        metadata={"sender": sender, "content": msg.payload}
    )
    
    # Log specific internal storage mutation action
    append_to_storage_bucket(
        ctx=ctx,
        bucket_name="action_logs",
        action="MUTATE_INBOUND_QUEUE",
        metadata={"status": "success"}
    )

# Explicit function to showcase user import tracking
def import_user_profile_logs(ctx: Context, user_id: str, log_payload: str):
    """Call this whenever users upload or import system data."""
    append_to_storage_bucket(
        ctx=ctx,
        bucket_name="user_import_logs",
        action="USER_MANUAL_IMPORT",
        metadata={"user_id": user_id, "data_summary": log_payload}
    )
    ctx.logger.info(f"User import saved for profile: {user_id}")


# --- 4. The 90-Day Automatic Reset & Garbage Collector ---
@storage_agent.on_interval(period=CLEANUP_INTERVAL_SECONDS)
async def automatic_garbage_collector(ctx: Context):
    """Scans all partitions, drops items > 90 days old, and cleans disk state."""
    ctx.logger.info("🧹 Initiating automated 90-day rolling data purge...")
    
    now = time.time()
    target_buckets = ["sent_info", "received_info", "user_import_logs", "action_logs"]
    total_purged_items = 0
    
    for bucket in target_buckets:
        raw_records = ctx.storage.get(bucket) or []
        
        # Keep entries where current time minus log time is LESS than 90 days
        fresh_records = [
            record for record in raw_records 
            if (now - record["timestamp"]) < RETENTION_TTL_SECONDS
        ]
        
        purged_count = len(raw_records) - len(fresh_records)
        total_purged_items += purged_count
        
        # Reset storage partition with clean, filtered dataset
        ctx.storage.set(bucket, fresh_records)
        
        if purged_count > 0:
            ctx.logger.info(f"Removed {purged_count} garbage records from '{bucket}'")

    ctx.logger.info(f"✨ Garbage collection completed. Total records permanently destroyed: {total_purged_items}")

if __name__ == "__main__":
    storage_agent.run()
