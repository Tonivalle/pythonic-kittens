from pythonic_kittens.game import build_game_from_players
from pythonic_kittens.player import Player


class TestGameFactory:
    game = build_game_from_players(players=[Player("Andrew"), Player("Pepe")])

    def test_player_names_are_in_game(self):
        assert all(name in self.game.player_names for name in ("Andrew", "Pepe"))

    def test_players_all_have_defuse(self):
        assert all(player.has_defuse for player in self.game.players)

    def test_players_all_have_8_cards(self):
        assert all(player.hand_size == 8 for player in self.game.players)

    def test_deck_size_is_correct(self):
        assert self.game.deck.size == 29

    def test_discard_pile_starts_empty(self):
        assert self.game.discard_pile.size == 0
