import asyncio
import websockets
import aioconsole

async def connect_to_server():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
    # Enviar un mensaje al servidor
        message = await aioconsole.ainput("Enter message to send: ")
        if(message == "left"):
            await websocket.send('left')
        if(message == "right"):
            await websocket.send('right')
        print("Message sent to server: prueba")

        # Recibir el mensaje del servidor
        response = await websocket.recv()
        print(f"Message received from server: {response}")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_server())
