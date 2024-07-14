import asyncio
import importlib
import websockets
import resultados
import sys
sys.path.append('../../')
from BrailleWrapper import guardarArchivo
# A set to store connected clients
connectedClients = []
async def handler(websocket, path):
    connectedClients.append(websocket)
    index = 0
    try:
        async for message in websocket:
            importlib.reload(resultados)
            resultBraille = resultados.brailleList
            sendLine = "\n".join(resultBraille[index])
            if(message == "start"):
                await connectedClients[0].send(sendLine)
            if(message == "finish"):
                sendLine = ''.join(['0' if char != '\n' else char for char in sendLine])
                listSendLine = sendLine.split('\n')
                listSendLine = [listSendLine]
                guardarArchivo(listSendLine)
                await connectedClients[0].send(sendLine)
            if(message == "right" and index<len(resultBraille) - 1):
                index +=1
                sendLine = "\n".join(resultBraille[index])
                await websocket.send(sendLine)
            elif(message == "left" and index>0):
                index -=1
                sendLine = "\n".join(resultBraille[index])
                await websocket.send(sendLine)
            else:
                sendLine = "\n".join(resultBraille[index])
                await websocket.send(sendLine)
            print("Enviando")
            print("Estado actual: " + message)
            print("Pagina: "  + str(index) + " de " + str(len(resultBraille)))
    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        connectedClients.remove(websocket)


def start_server():
    server = websockets.serve(handler, "localhost", 8080)
    asyncio.get_event_loop().run_until_complete(server)
    print("WebSocket server is running on ws://localhost:8080")
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    start_server()
