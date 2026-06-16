from uagents import Protocol
from protocols.messages import CallRequest, UserImportLog

# Create a dedicated protocol for data lifecycle events
storage_proto = Protocol(name="StorageLifecycleProtocol", version="1.0.0")

# Note: Handlers will be attached to this protocol dynamically in the next steps
