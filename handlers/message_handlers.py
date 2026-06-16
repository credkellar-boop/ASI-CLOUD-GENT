from uagents import Context
from protocols.storage_protocol import storage_proto
from protocols.messages import CallRequest, CallResponse
from utils.helpers import append_to_bucket

@storage_proto.on_message(model=CallRequest, replies=CallResponse)
async def handle_remote_call(ctx: Context, sender: str, msg: CallRequest):
    ctx.logger.info(f"📥 Processing command: '{msg.command}' from {sender}")
    
    # 1. Log inbound transaction information
    append_to_bucket(ctx, "received_info", "INBOUND_CALL", {"from": sender, "cmd": msg.command})
    
    # 2. Execute command logic
    execution_status = f"Executed: {msg.command}"
    
    # 3. Log outbound reply information
    append_to_bucket(ctx, "sent_info", "OUTBOUND_REPLY", {"to": sender, "status": execution_status})
    
    # 4. Return structural response
    return CallResponse(status="SUCCESS", payload={"result": execution_status})
