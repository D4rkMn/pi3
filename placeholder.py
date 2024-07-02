import asyncio
import websockets
import aioconsole

async def connect_to_server():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        message = "PalabraImposibleDeAdivinar"
        while True:
            # Enviar un mensaje al servidor
            if(message ==  "PalabraImposibleDeAdivinar"):
                await websocket.send(message)
                response = await websocket.recv()
                print(f"Message received from server: {response}")
            message = await aioconsole.ainput("Enter message to send: ")
            
            if message == "end":
                break
            if message in ["left", "right"]:
                await websocket.send(message)
                print(f"Message sent to server: {message}")
            
                # Recibir el mensaje del servidor
                response = await websocket.recv()
                print(f"Message received from server: {response}")
            else:
                print("Invalid message. Please enter 'left' or 'right'.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_server())
