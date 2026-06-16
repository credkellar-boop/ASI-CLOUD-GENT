from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter(tags=["Streaming"])

class WebSocketLogManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def stream_system_event(self, event_message: str):
        """Broadcasts internal agent events directly to monitoring clients."""
        for connection in self.active_connections:
            try:
                await connection.send_text(event_message)
            except Exception:
                # Handle dropped pipes gracefully
                pass

stream_manager = WebSocketLogManager()

@router.websocket("/ws/events")
async def websocket_endpoint(websocket: WebSocket):
    await stream_manager.connect(websocket)
    try:
        while True:
            # Keep connection alive, listen for client heartbeats
            await websocket.receive_text()
    except WebSocketDisconnect:
        stream_manager.disconnect(websocket)
