from dataclasses import dataclass, field
from typing import Any


@dataclass
class Player:
    """
    Player for the game.
    """

    name: str
    """
    Name of the player
    """
    score: int = field(default=0, init=False)
    """
    Score of the player
    """
    hand: list[Any] = field(default_factory=list, init=False)
    """
    Current cards the player has available.
    """
