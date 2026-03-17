from fastapi import WebSocket

class WebSocketManager:

    def __init__(self):
        # user_id -> websocket connection
        self.active_connections = {}
    
    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_to_user(self, user_id: str, message: dict):
        websocket = self.active_connections.get(user_id)

        if websocket:
            await websocket.send_json(message)

websocket_manager = WebSocketManager()
