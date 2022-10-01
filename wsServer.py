import websockets
import asyncio

PORT = 7890

connected = set()

async def echo(websocket, path):
    print("A Client just connected")
    connected.add(websocket)
    try:
        async for message in websocket:
            print("Recieved a message from a Client: "+message)
            #await websocket.send(message)
            for ws in connected:
                if ws != websocket:
                    await ws.send(message)
            
    except websockets.exceptions.ConnectionClosed:
        print("A Client just disconnected")
    except:
        print("Something went wrong")
    finally:
        connected.remove(websocket)
            


start_server = websockets.serve(echo,"localhost",PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

