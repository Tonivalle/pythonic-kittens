from dataclasses import dataclass, field

from pythonic_kittens.cards import Card, CardKind


@dataclass
class Player:
    """
    Player for the game.
    """

    name: str
    """
    Name of the player
    """
    score: int = field(default=0, init=False)
    """
    Score of the player
    """
    hand: list[Card] = field(default_factory=list, init=False)
    """
    Current cards the player has available.
    """

    @property
    def has_defuse(self) -> bool:
        """
        Returns True if any card in the players hand is a defuse.
        """
        return any(card.kind == CardKind.DEFUSE for card in self.hand)

    @property
    def hand_size(self) -> int:
        """
        Returns the number of cards the player has.
        """
        return len(self.hand)
