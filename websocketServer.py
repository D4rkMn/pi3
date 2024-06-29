import asyncio
import websockets
from resultados import brailleList
# A set to store connected clients
connected_clients = set()
async def handler(websocket, path):
    connected_clients.add(websocket)
    resultBraille = brailleList
    index = 1
    async for message in websocket:
        print("Sending resultBraille to client")
        print("Received: " + message)
        if(message == "left"):
            index -=1
            
            print("Pagina: " + str(index))
        elif message == "right":
            index +=1
            print("Pagina: " + str(index))
            

def start_server():
    start_server = websockets.serve(handler, "0.0.0.0", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server is running on ws://localhost:8080")
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    start_server()