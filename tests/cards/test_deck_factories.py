import pytest

from pythonic_kittens.cards.factories import generate_deck_from_players


@pytest.mark.parametrize(
    "n_players, total_cards", [(2, 45), (3, 46), (4, 72), (5, 73), (6, 74), (7, 75), (8, 120), (9, 121), (10, 122)]
)
def test_factory_creates_correct_deck_for_n_players(n_players, total_cards):
    deck = generate_deck_from_players(n_players=n_players)
    assert len(deck.cards) == total_cards


def test_factory_raises_if_more_than_10_players():
    with pytest.raises(ValueError, match="Number of players"):
        generate_deck_from_players(n_players=11)
