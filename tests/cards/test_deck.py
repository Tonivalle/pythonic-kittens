from pythonic_kittens.cards.cards import CardKind
from pythonic_kittens.cards.factories import generate_deck_from_players
from copy import deepcopy

class TestDeck:
    sample_deck = generate_deck_from_players(n_players=10)

    def test_deck_can_shuffle(self):
        original_deck = deepcopy(self.sample_deck)
        assert self.sample_deck.shuffle() != original_deck
    
    def test_deck_can_peek(self):
        assert self.sample_deck.peek(3) == self.sample_deck.cards[:3]
    
    def test_deck_can_draw(self):
        cards = self.sample_deck.draw(3)
        assert all(card.kind == CardKind.DEFUSE for card in cards)
        assert len(self.sample_deck.cards) == 119
