from Card import Card
class Player:
    def __init__(self,id:int)->None:
        self.id = id
        self.hand = []
        self.hand.append(id)
    
    def addCard(self,card:Card)->None:
        self.hand.append(card)
    
    def addCard(self,cardList:list)->None:
        self.hand = self.hand + cardList
