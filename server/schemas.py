from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class SecuritySettingsUpdate(BaseModel):
    enable_auto_patch: bool = Field(default=False)
    alert_webhook_url: Optional[str] = None

class StorageStatusResponse(BaseModel):
    bucket_name: str
    record_count: int
    bytes_used: int
    oldest_record_timestamp: Optional[float]
