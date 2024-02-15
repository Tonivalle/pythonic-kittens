from pythonic_kittens.player.player import Player


class TestPlayer:
    def test_player_correctly_initializes(self):
        player = Player(name="Pipo")

        assert player.name == "Pipo"
        assert player.score == 0
        assert len(player.hand) == 0
