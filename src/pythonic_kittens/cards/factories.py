from itertools import chain

from pythonic_kittens.cards.cards import Card, CardKind
from pythonic_kittens.cards.deck import Deck

DeckSize = dict[CardKind, int]


def generate_deck_from_players(n_players: int) -> Deck:
    """
    Depending on the number of players, the deck will have a different number of cards.
    """
    deck_size = _select_deck_size(n_players)

    exploding_kitten_cards = _generate_exploding_kittens(n_players)
    base_cards = _generate_base_cards(deck_size)

    return Deck(cards=base_cards + exploding_kitten_cards)


def _select_deck_size(n_players: int) -> DeckSize:
    if 2 <= n_players <= 3:
        return small_deck
    if n_players <= 7:
        return medium_deck
    if n_players <= 10:
        return big_deck
    raise ValueError(f"Number of players {n_players} not supported.")


def _generate_exploding_kittens(n_players: int) -> list[Card]:
    return [Card(CardKind.EXPLODING_KITTEN) for _ in range(n_players - 1)]


def _generate_base_cards(deck_size: DeckSize) -> list[Card]:
    expanded_card_kind_iterable = ((kind,) * deck_size[kind] for kind in deck_size)
    return [Card(card_kind) for card_kind in chain.from_iterable(expanded_card_kind_iterable)]


small_deck = {
    CardKind.DEFUSE: 3,
    CardKind.SKIP: 4,
    CardKind.FAVOR: 2,
    CardKind.NOPE: 4,
    CardKind.ATTACK: 4,
    CardKind.FERAL_CAT: 2,
    CardKind.SHUFFLE: 2,
    CardKind.SEE_THE_FUTURE: 3,
    CardKind.ALTER_THE_FUTURE: 2,
    CardKind.DRAW_FROM_BOTTOM: 3,
    CardKind.CAT_1: 3,
    CardKind.CAT_2: 3,
    CardKind.CAT_3: 3,
    CardKind.CAT_4: 3,
    CardKind.CAT_5: 3,
}

medium_deck = {
    CardKind.DEFUSE: 7,
    CardKind.SKIP: 6,
    CardKind.FAVOR: 4,
    CardKind.NOPE: 6,
    CardKind.ATTACK: 7,
    CardKind.FERAL_CAT: 4,
    CardKind.SHUFFLE: 4,
    CardKind.SEE_THE_FUTURE: 3,
    CardKind.ALTER_THE_FUTURE: 4,
    CardKind.DRAW_FROM_BOTTOM: 4,
    CardKind.CAT_1: 4,
    CardKind.CAT_2: 4,
    CardKind.CAT_3: 4,
    CardKind.CAT_4: 4,
    CardKind.CAT_5: 4,
}

big_deck = {
    CardKind.DEFUSE: 10,
    CardKind.SKIP: 10,
    CardKind.FAVOR: 6,
    CardKind.NOPE: 10,
    CardKind.ATTACK: 11,
    CardKind.FERAL_CAT: 6,
    CardKind.SHUFFLE: 6,
    CardKind.SEE_THE_FUTURE: 6,
    CardKind.ALTER_THE_FUTURE: 6,
    CardKind.DRAW_FROM_BOTTOM: 7,
    CardKind.CAT_1: 7,
    CardKind.CAT_2: 7,
    CardKind.CAT_3: 7,
    CardKind.CAT_4: 7,
    CardKind.CAT_5: 7,
}
