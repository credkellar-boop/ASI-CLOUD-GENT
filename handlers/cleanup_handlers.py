import time
from uagents import Context
from protocols.storage_protocol import storage_proto
import config

@storage_proto.on_interval(period=config.CLEANUP_INTERVAL_SECONDS)
async def maintenance_purge_worker(ctx: Context):
    ctx.logger.info("🧹 Initializing scheduled 90-day rolling data purge...")
    
    current_time = time.time()
    target_partitions = ["sent_info", "received_info", "user_import_logs", "action_logs"]
    purged_count = 0
    
    for bucket in target_partitions:
        raw_history = ctx.storage.get(bucket) or []
        
        # Filter out any records that exceed the 90-day retention threshold
        retained_records = [
            record for record in raw_history
            if (current_time - record["timestamp"]) < config.RETENTION_TTL_SECONDS
        ]
        
        dropped = len(raw_history) - len(retained_records)
        purged_count += dropped
        
        # Commit the cleaned data partition back to memory
        ctx.storage.set(bucket, retained_records)
        
        if dropped > 0:
            ctx.logger.info(f"Purged {dropped} expired records from bucket: '{bucket}'")
            
    ctx.logger.info(f"✨ Purge complete. Garbage items destroyed: {purged_count}")
