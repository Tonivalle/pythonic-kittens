from dataclasses import dataclass, field

from pythonic_kittens.cards.cards import Card


@dataclass
class DiscardPile:
    """
    Cards that have been played.
    """

    cards: list[Card] = field(default_factory=list)

    @property
    def size(self):
        """
        Size of the discard pile
        """
        return len(self.cards)
