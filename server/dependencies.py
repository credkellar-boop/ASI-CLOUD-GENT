import os
from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "X-ASI-ADMIN-TOKEN"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_api_access_token(api_key: str = Security(api_key_header)):
    """Validates header credentials before granting access to the agent dashboard."""
    expected_token = os.getenv("MANAGEMENT_API_KEY", "default_admin_secure_passphrase")
    
    if api_key != expected_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Denied: Invalid Infrastructure Management Key Header."
        )
    return api_key
