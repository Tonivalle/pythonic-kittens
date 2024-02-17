import random
from dataclasses import dataclass

from pythonic_kittens.cards.cards import Card


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
    def size(self):
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
