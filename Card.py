from CardEssentials import SUIT,TYPE
class Card:
    
    def __init__(self,suit:SUIT,CardType:TYPE)->None:
        self.SUIT = suit
        self.TYPE = CardType
    
    def __str__(self)->str:
        return f'{self.TYPE} OF {self.SUIT}'

c1 = Card(SUIT.HEARTS,TYPE.ACE)
c2 = Card(SUIT.HEARTS,TYPE.TEN)


print(int(c1.TYPE)+0)
