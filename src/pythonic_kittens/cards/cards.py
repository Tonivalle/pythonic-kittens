from dataclasses import dataclass
from enum import StrEnum, auto


class CardKind(StrEnum):
    """
    Possible types of cards.
    """

    EXPLODING_KITTEN = auto()
    DEFUSE = auto()
    SKIP = auto()
    FAVOR = auto()
    NOPE = auto()
    ATTACK = auto()
    FERAL_CAT = auto()
    SHUFFLE = auto()
    SEE_THE_FUTURE = auto()
    ALTER_THE_FUTURE = auto()
    DRAW_FROM_BOTTOM = auto()
    CAT_1 = auto()
    CAT_2 = auto()
    CAT_3 = auto()
    CAT_4 = auto()
    CAT_5 = auto()


@dataclass
class Card:
    """
    Card object.
    """

    kind: CardKind
