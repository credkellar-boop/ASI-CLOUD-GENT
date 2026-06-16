from uagents import Agent, Context
import config
from protocols.messages import CallRequest, CallResponse
from utils.helpers import append_to_bucket

storage_agent = Agent(
    name="storage_worker",
    seed=config.AGENT_SEED,
    port=config.PORT,
    endpoint=[config.ENDPOINT]
)

@storage_agent.on_event("startup")
async def init_storage(ctx: Context):
    buckets = ["sent_info", "received_info", "user_import_logs", "action_logs"]
    for bucket in buckets:
        if not ctx.storage.get(bucket):
            ctx.storage.set(bucket, [])
    ctx.logger.info(f"Storage Node online at address: {storage_agent.address}")
