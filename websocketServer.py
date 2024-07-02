import asyncio
import websockets
from resultados import brailleList
# A set to store connected clients
connected_clients = set()
async def handler(websocket, path):
    connected_clients.add(websocket)
    resultBraille = brailleList
    index = 0
    sendLine=""
    for character in resultBraille[index]:
        sendLine += character
        sendLine += '\n'
    filtro = False
    async for message in websocket:
        print("Sending resultBraille to client")
        print("Received: " + message)
        print(str(len(brailleList)) + " " + str(index))
        if(message == "PalabraImposibleDeAdivinar"):
            filtro =True
            await websocket.send(sendLine)
        elif(message == "left" and index>0):
            index -=1
        elif message == "right" and index + 1<len(brailleList):
            index +=1
        sendLine = ""
        for character in resultBraille[index]:
            sendLine += character
            sendLine += '\n'
        if(filtro == False):
            await websocket.send(sendLine)
        filtro = False
        
            

def start_server():
    start_server = websockets.serve(handler, "0.0.0.0", 8080)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server is running on ws://localhost:8080")
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    start_server()