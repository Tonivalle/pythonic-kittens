from pythonic_kittens.cards import CardKind, DiscardPile, generate_deck_from_players
from pythonic_kittens.game import Game
from pythonic_kittens.player import Player


def build_game_from_players(players: list[Player]) -> Game:
    """
    Generate a game instance from player instances or names.
    """

    game = Game(
        players=players,
        turn_order=players.copy(),
        deck=generate_deck_from_players(n_players=len(players)),
        discard_pile=DiscardPile(),
    )

    game.deck.shuffle()

    defuses = game.deck.extract_card_kind(kind=CardKind.DEFUSE, n_cards=len(game.players))
    for player, card in zip(game.players, defuses):
        player.hand.append(card)
        player.hand.extend(game.deck.draw(n_cards=7))

    return game
