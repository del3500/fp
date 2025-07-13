import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2,11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
  def __len__(self):
    return len(self._cards)

  def __getitem__(self, position):
    return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# e.g.,
# 5(rank) * 4(length of suits) + 0(club)   # 5 of clubs     = 16 
# K(rank 11) * 4(length of suits) + 3(spades) # K of spades = 47  

def spades_high(card):
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value * len(suit_values) + suit_values[card.suit]

  







