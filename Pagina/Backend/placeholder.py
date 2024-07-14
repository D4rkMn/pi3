import asyncio
import websockets
import aioconsole

async def recibirMensajes(websocket):
    while True:
        response = await websocket.recv()
        print(f"Message received from server: \n{response}")
        if response == "finish":
            return response

async def enviarMensajes(websocket):
    while True:
        message = await aioconsole.ainput("")
        if message in ["left", "right"]:
            await websocket.send(message)
            print(f"Message sent to server: {message}")
        else:
            print("Invalid message. Please enter 'left' or 'right'.")
# corre placholder.py y prueba con "left" y "right"
async def arduinoClient():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        response =await websocket.recv()
        print(response)
        recibirTask = asyncio.create_task(recibirMensajes(websocket))
        enviarTask = asyncio.create_task(enviarMensajes(websocket))
        done, pending = await asyncio.wait(
            [recibirTask, enviarTask],
            return_when=asyncio.FIRST_COMPLETED
        )
        for task in pending:
            task.cancel()

        if recibirTask in done and recibirTask.result() == "finish":
            print("Fue ps")
        else:
            await recibirTask 
if __name__ == "__main__":
    asyncio.run(arduinoClient())
