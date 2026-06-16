from fastapi import APIRouter, HTTPException
from server.schemas import SecuritySettingsUpdate, StorageStatusResponse
from utils.security_auditor import run_infrastructure_audit
import config

router = APIRouter(prefix="/api/v1")

@router.get("/security/audit", tags=["Security"])
def get_security_audit():
    """Triggers and returns an instantaneous infrastructure compliance scan."""
    return run_infrastructure_audit()

@router.post("/security/settings", tags=["Security"])
def update_security_settings(settings: SecuritySettingsUpdate):
    """Allows runtime configuration changes for security tracking engines."""
    # Logic to persist settings changes dynamically
    return {"status": "UPDATED", "config": settings.dict()}
