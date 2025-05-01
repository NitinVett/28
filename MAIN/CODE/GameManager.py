from .CardManager import CardManager
from .Player import Player
from .Card import Card
from .CardEssentials import SUIT
class GameManager:

    def __init__(self,playerList:list[Player],manager:CardManager):
        self.drum:SUIT = None
        self.turnOrder:list[Player] = playerList
        self.team1Hands:list[Card] = []
        self.team2Hands:list[Card] = []
        self.currentHand:list[Card] = []
        self.cardManager:CardManager = manager
    

    def executeTurn(self):
        for player in self.turnOrder:
            selectedCard = self.handleUserInput(player)
            self.currentHand.append((player,selectedCard))
        
        winningPlayer = self.evaluateWinningCard(self.currentHand)
        playerPos = self.getPlayerPosition(winningPlayer,self.turnOrder)
        self.turnOrder = self.adjustTurnOrder(playerPos,self.turnOrder)
        if winningPlayer.id%2 == 0:
            self.team1Hands = self.team1Hands + self.currentHand
        else:
            self.team2Hands = self.team1Hands + self.currentHand
        self.currentHand = []
            
    
    def getPlayerPosition(self,player:Player,currentOrder:list[Player]):
         for i,p in enumerate(currentOrder):
            if p == player:
                return i
        
    def adjustTurnOrder(self,shift:int,currentOrder:list[Player]) -> list[Player]:
        newTurnOrder = [None,None,None,None]

        for i in range(len(currentOrder)):
            newTurnOrder[(i+shift)%len(currentOrder)] = currentOrder[i]
        
        return newTurnOrder
        
    
    def evaluateWinningCard(self,currentHand:list[(Player,Card)]) -> Player:
        maxCard = currentHand[0][1]
        winningPlayer = currentHand[0][0]
        for player,card in currentHand[1:]:
            if maxCard.SUIT == card.SUIT or card.SUIT == self.drum:
                if maxCard < card:
                    maxCard = card
                    winningPlayer = player
        return winningPlayer

                
    def handleUserInput(self,player:Player) -> Card:
        while True:
            try:
                print(player.hand)
                choice = int(input("Please enter the index of the card you want to choose(1 indexed)"))
                if choice < 1 or choice > len(player.hand):
                    assert("Invalid choice")
                return player.hand.pop(choice)
            except Exception as e:
                print(e)
            