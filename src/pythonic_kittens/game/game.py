from dataclasses import dataclass

from pythonic_kittens.cards import Deck
from pythonic_kittens.cards.discard import DiscardPile
from pythonic_kittens.player import Player


@dataclass
class Game:
    """
    Game instance that handles turns, player actions and reactions.
    """

    players: list[Player]
    """
    Players for the game.
    """

    turn_order: list[Player]
    """
    Turn order for the game.

    Can be bigger than the player list (for example after an Attack).
    """

    deck: Deck
    discard_pile: DiscardPile
