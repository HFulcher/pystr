import uvicorn
import logging
from events import Event
from requests import Request
from fastapi import FastAPI, WebSocket
from ConnectionManager import ConnectionManager

logger = logging.getLogger('uvicorn')

app = FastAPI()
manager = ConnectionManager()


# Thanks to https://code.pobblelabs.org/fossil/nostr_relay/ for this
def validate_message(message):
    if not isinstance(message, list):
        return False
    if len(message) < 2:
        return False
    if message[0] not in ("REQ", "EVENT", "CLOSE"):
        return False

    return True


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket, client_pub: int):
    await manager.connect(websocket)
    await manager.broadcast(f'Client {client_pub} connected')

#    try:
    while True:
        data = await websocket.receive_json()

        if validate_message(data):
            match data[0]:
                case "REQ":
                    # TODO: Need to query internal database and return matching events
                    response = str(Request(subscription_id=data[1], filters=**data[2]))
                case "EVENT":
                    response = str(Event(**data[1]))
                case "CLOSE":
                    response = "Received CLOSE call"

            await manager.send_personal_message(response, websocket)

        else:
            await manager.send_personal_message("Incorrect format", websocket)

#    except Exception as e:
#        logger.error(f"Error in connection with {client_pub}")
#        logger.error(e)
