from pythonic_kittens.game import build_game_from_players
from pythonic_kittens.player import Player


def test_factory_builds_game_correctly_with_player_objects():
    players = [Player("Andrew"), Player("Pepe")]
    game = build_game_from_players(players=players)
    assert game.players == [Player("Andrew"), Player("Pepe")]
    assert game.deck.size == 45
    assert game.discard_pile.size == 0
