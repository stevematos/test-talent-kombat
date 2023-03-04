from config.environment import API_VERSION, APP_NAME, DEBUG_MODE
from fastapi import FastAPI
from routers import game

# Core Application Instance
app = FastAPI(title=APP_NAME, version=API_VERSION, debug=DEBUG_MODE)

app.include_router(game.router, prefix="/game", tags=["game"])
