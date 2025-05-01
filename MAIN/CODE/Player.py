from .Card import Card
class Player:

    # Initializes a player with a given id and an empty hand
    def __init__(self,id:int)->None:
        self.id:int = id
        self.hand:list[Card] = []
        
    # Appends a card to players hand
    def addCard(self,card:Card)->None:
        self.hand.append(card)
    
    def __eq__(self, value):
        return self.id == value.id

