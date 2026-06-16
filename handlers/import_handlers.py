from uagents import Context
from protocols.storage_protocol import storage_proto
from protocols.messages import UserImportLog
from utils.helpers import append_to_bucket

@storage_proto.on_message(model=UserImportLog)
async def handle_user_import(ctx: Context, sender: str, msg: UserImportLog):
    ctx.logger.info(f"💾 Processing manual log import for User: {msg.user_id}")
    
    # Isolate user-supplied data streams entirely within the user_import_logs partition
    append_to_bucket(
        ctx=ctx,
        bucket_name="user_import_logs",
        action="USER_DATA_IMPORT",
        metadata={"user_id": msg.user_id, "raw_payload": msg.log_data}
    )
    
    append_to_bucket(ctx, "action_logs", "MUTATE_USER_BUCKET", {"user_id": msg.user_id})
