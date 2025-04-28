from CardEssentials import SUIT,TYPE
class Card:
    
    # Initializes a cards suit and type
    def __init__(self,suit:SUIT,CardType:TYPE)->None:
        self.SUIT = suit
        self.TYPE = CardType
    
    # String representation of a Card
    def __str__(self)->str:
        return f'{self.TYPE} OF {self.SUIT}'

c1 = Card(SUIT.HEARTS,TYPE.ACE)
c2 = Card(SUIT.HEARTS,TYPE.TEN)


print(int(c1.TYPE)+0)
