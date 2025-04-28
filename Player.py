from Card import Card
class Player:

    # Initializes a player with a given id and an empty hand
    def __init__(self,id:int)->None:
        self.id = id
        self.hand = []
        
    # Appends a card to players hand
    def addCard(self,card:Card)->None:
        self.hand.append(card)
    
    # Appends a list of cards to a players hand
    def addCard(self,cardList:list)->None:
        self.hand = self.hand + cardList
