from uagents import Model
from typing import Optional, Dict, Any

class CallRequest(Model):
    command: str
    metadata: Optional[Dict[str, Any]] = None

class CallResponse(Model):
    status: str
    payload: Optional[Dict[str, Any]] = None

class UserImportLog(Model):
    user_id: str
    log_data: str
