import json
from multiprocessing import Queue

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from fastapi.responses import RedirectResponse

from starlette.staticfiles import StaticFiles

def run_fastapi(web):
    """Run FastAPI server from both web and websocket"""
    app = FastAPI()

    @app.get("/", response_class=RedirectResponse)
    def root():
        return "/index.html"

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        data = await websocket.receive_json()

    app.mount("/", StaticFiles(directory=web), name="web")

    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    run_fastapi(web='web')
