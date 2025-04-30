from .CardEssentials import SUIT,TYPE
from functools import total_ordering

@total_ordering
class Card:
    
    # Initializes a cards suit and type
    def __init__(self,suit:SUIT,CardType:TYPE)->None:
        self.SUIT:SUIT = suit
        self.TYPE:TYPE = CardType
        
    
    # String representation of a Card
    def __str__(self)->str:
        return f'{self.TYPE} OF {self.SUIT}'

    def __eq__(self, card):
        return self.TYPE.value == card.TYPE.value

    def __lt__(self, card):
        return self.TYPE.value < card.TYPE.value
    
    def __gt__(self, card):
        return self.TYPE.value > card.TYPE.value
        
