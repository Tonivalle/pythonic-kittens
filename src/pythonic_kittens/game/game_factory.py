from pythonic_kittens.cards import DiscardPile, generate_deck_from_players
from pythonic_kittens.game import Game
from pythonic_kittens.player import Player


def build_game_from_players(players: list[Player]) -> Game:
    """
    Generate a game instance from player instances or names.
    """

    return Game(
        players=players,
        turn_order=players.copy(),
        deck=generate_deck_from_players(n_players=len(players)),
        discard_pile=DiscardPile(),
    )
