from config.exceptions import ActionExceedCharacters
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from services.game import start_game

router = APIRouter()


class GamePlayers(BaseModel):
    player_actions: dict[str, dict[str, list]]


@router.post("/start")
async def start(game_players: GamePlayers):
    try:
        messages = start_game(game_players.player_actions)
        return {"narration": messages}
    except ActionExceedCharacters as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.__str__())
