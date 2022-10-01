import websockets
import asyncio

PORT = 7890

async def echo(websocket, path):
    print("A Client just connected")

    async for message in websocket:

        print("Recieved a message from a Client: "+message)

        await websocket.send(message)
            


start_server = websockets.serve(echo,"localhost",PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

