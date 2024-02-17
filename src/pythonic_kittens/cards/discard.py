from dataclasses import dataclass, field

from pythonic_kittens.cards.card import Card


@dataclass
class DiscardPile:
    """
    Cards that have been played.
    """

    cards: list[Card] = field(default_factory=list)

    @property
    def size(self) -> int:
        """
        Size of the discard pile
        """
        return len(self.cards)
