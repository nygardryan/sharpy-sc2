import json
from typing import List, Dict, Optional
from uuid import uuid4

from sc2 import Race


class GameResult:
    game_started: str
    result: int  # -1 for defeat, 0 for draw, 1 for victory
    build_used: str
    enemy_build: int
    first_attacked: Optional[float]  # timing in game seconds when attacked
    game_duration: Optional[float]  # timing in game seconds when game ended
    enemy_race:  Optional[Race]  # enemy race in the selected game

    def __init__(self) -> None:
        self.guid = uuid4()
        self.game_started = ""
        self.result = 0
        self.build_used = ""
        self.enemy_build = 0
        self.first_attacked = None
        self.game_duration = None
        self.enemy_race = None


class OpponentData:
    enemy_id: str
    results: List[GameResult]

    def __init__(self) -> None:
        self.enemy_id = None
        self.results = []
        super().__init__()
