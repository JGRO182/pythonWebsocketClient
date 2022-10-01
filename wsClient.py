import websockets
import asyncio
import json
import math


# make sure the message contains a "x" and a "y" key with a digit value
def coordinatesValid(dict):
    if "x" in dict and "y" in dict:
        if type(dict["x"]) == float or int:
            if type(dict["y"]) == float or int:
                return True
    return False


def msgRecieved(message):
    print(message)

    # convert json to dict object
    dict = json.loads(message)

    # check if message contains a valid x and y value
    if coordinatesValid(dict):
        drawRect(50,15,1,dict)
    else:
        print(dict)


# draw the rectangle
def drawRect(width, height, borderwidth, relativPosition):

    # calculate the normal position from the relativ position + round 
    pos = {"x":math.floor(relativPosition["x"]*width),
    "y":math.floor(relativPosition["y"]*height)}


    for row in range(height):

        for column in range(width):

            #draw point
            if pos["x"] == column and pos["y"] == row:
                print("O", end="")

            #draw border
            elif row < borderwidth or row >= height - borderwidth or column < borderwidth or column >= width - borderwidth:
                print("#", end="")

            else:
                print(" ", end="")

        print("")  
    print(pos)
    print("") 
    


async def listen():
    url = "ws://websocket-server-canvas.glitch.me/"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            msgRecieved(msg)
            

asyncio.get_event_loop().run_until_complete(listen())

