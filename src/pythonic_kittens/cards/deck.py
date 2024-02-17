import random
from dataclasses import dataclass

from pythonic_kittens.cards.card import Card, CardKind


@dataclass
class Deck:
    """
    Deck of cards for the game.
    """

    cards: list[Card]
    """
    Cards contained in the deck.
    """

    def shuffle(self):
        """
        Shuffle the deck.
        """
        random.shuffle(self.cards)

    @property
    def size(self) -> int:
        """
        Size of the deck
        """
        return len(self.cards)

    def draw(self, n_cards: int = 1) -> list[Card]:
        """
        Remove the first n_cards from the deck and return them.
        """
        cards_to_return = self.cards[:n_cards]
        self.cards = self.cards[n_cards:]
        return cards_to_return

    def peek(self, n_cards: int) -> list[Card]:
        """
        Return the first n_cards from the deck (without removing them from the deck).
        """
        return self.cards[:n_cards]

    def extract_card_kind(self, kind: CardKind, n_cards: int) -> list[Card]:
        """
        get a specific card kind from deck and returns them.
        """
        cards_to_return, cards_remaining = self._extract_cards(kind, n_cards)
        self.cards = cards_remaining
        return cards_to_return

    def _extract_cards(self, kind: CardKind, n_cards: int) -> tuple[list[Card], list[Card]]:
        cards_to_return = []
        cards_remaining = []
        count = 0
        for card in self.cards:
            if card.kind == kind and count < n_cards:
                cards_to_return.append(card)
                count += 1
            else:
                cards_remaining.append(card)
        return cards_to_return, cards_remaining
