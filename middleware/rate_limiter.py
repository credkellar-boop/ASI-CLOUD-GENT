import time
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

class CloudRateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.limit = requests_per_minute
        self.client_records = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        
        # Clean record history window
        self.client_records = {ip: ts for ip, ts in self.client_records.items() if current_time - ts < 60}
        
        if client_ip in self.client_records and len(self.client_records[client_ip]) >= self.limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Infrastructure entry point throttled."
            )
            
        self.client_records.setdefault(client_ip, []).append(current_time)
        return await call_next(request)
