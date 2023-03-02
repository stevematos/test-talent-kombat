from fastapi import APIRouter

from pydantic import BaseModel

from services.game import start_game

router = APIRouter()


class GamePlayers(BaseModel):
    player_movements: dict[str, dict[str, list]]


@router.post("/start")
async def start(game_players: GamePlayers):
    messages = start_game(game_players.player_movements)
    return {'narration': messages}
