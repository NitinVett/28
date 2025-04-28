from enum import Enum, auto

class SUIT(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()
    
    # String representation of SUIT enum
    def __str__(self) -> str:
        return self.name
    
class TYPE(Enum):

    # defines which cards beat one another (ex. Nine>ACE)
    SEVEN = auto(1)
    EIGHT = auto(2)
    QUEEN = auto(3)
    KING = auto(4)
    TEN = auto(5)
    ACE = auto(6)
    NINE = auto(7)
    JACK = auto(8)

    # String representation of TYPE enum
    def __str__(self) -> str:
        return self.name
    
    # defines the point value of each card
    def __int__(self) -> int:
        values = {
            TYPE.SEVEN: 0,
            TYPE.EIGHT: 0,
            TYPE.NINE: 2,
            TYPE.TEN: 1,
            TYPE.JACK: 3,
            TYPE.QUEEN: 0,
            TYPE.KING: 0,
            TYPE.ACE: 1,
        }
        return values[self]
    
