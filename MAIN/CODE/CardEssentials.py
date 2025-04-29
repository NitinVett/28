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
    SEVEN = 1
    EIGHT = 2
    QUEEN = 3
    KING = 4
    TEN = 5
    ACE = 6
    NINE = 7
    JACK = 8

    # String representation of TYPE enum
    def __str__(self) -> str:
        return self.name
    

    
