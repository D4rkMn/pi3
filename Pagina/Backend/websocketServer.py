import asyncio
import websockets

# A set to store connected clients
connected_clients = set()

async def handler(websocket, path):
    # Register the new client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            # Broadcast the message to all connected clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        # Unregister the client
        connected_clients.remove(websocket)

def start_server():
    start_server = websockets.serve(handler, "0.0.0.0", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server is running on ws://localhost:8080")
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    start_server()