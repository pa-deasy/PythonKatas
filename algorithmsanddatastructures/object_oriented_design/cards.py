from dataclasses import dataclass
from enum import Enum
from typing import List


# 7.1 - Deck of Cards: Design the data structures for a generic deck of cards.
class Suit(Enum):
    Spades = 0
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    

@dataclass
class Card:
    available: bool = True
    face_value: int  # 2 -> 10, 11 for Jack, 12 for Queen, 13 for King, 1 for Ace
    suit: Suit
    
    
class Deck:
    cards: List[Card]
    dealt_index = 0
    
    def __init__(self, cards) -> None:
        self.cards = cards
    
    def shuffle(self) -> None:
        # shuffle self.cards
        return
    
    def remaining_cards(self) -> int:
        return len(self.cards) - self.dealt_index
    
    def deal_hand(self, size: int) -> List[Card]:
        hand = self.cards[:size]
        self.cards = self.cards[size:]
        
        return hand
    
    def deal_card(self) -> Card:
        return self.cards.pop(0)
    

class Hand:
    cards: List[Card]
    
    def score(self) -> int:
         values = [c.face_value for c in self.cards]
         return sum(values)
     
    def add(self, card: Card) -> None:
        self.cards.append(card)
        
    def remove(self, card: Card) -> None:
        self.cards = [c for c in self.cards if c.face_value != card.face_value and c.suit != card.suit]
        