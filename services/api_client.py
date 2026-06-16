import httpx
from utils.logger import setup_production_logger

logger = setup_production_logger("api_client")

async def dispatch_cloud_alert(webhook_url: str, alert_payload: dict) -> bool:
    """Asynchronously dispatches operational threat matrices out to configured webhooks."""
    if not webhook_url:
        return False
        
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.post(webhook_url, json=alert_payload)
            if response.status_code == 200:
                return True
            logger.error(f"Failed to post external alert. Status: {response.status_code}")
        except Exception as e:
            logger.error(f"Exception encountered during alert dispatch: {str(e)}")
            
    return False
