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
        
    
    def startGame(self):
        CardManager.dealCards(self.turnOrder)
        self.playerCall()
        
    
   
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
            
    
    def getPlayerPosition(self,player:Player):
         for i,p in enumerate(self.turnOrder):
            if p == player:
                return i
        
    def adjustTurnOrder(self,shift:int) -> list[Player]:
        newTurnOrder = [None,None,None,None]

        for i in range(len(self.turnOrder)):
            newTurnOrder[(i+shift)%len(self.turnOrder)] = self.turnOrder[i]
        
        return newTurnOrder
        
    
    def evaluateWinningCard(self) -> Player:
        maxCard = self.currentHand[0][1]
        winningPlayer = self.currentHand[0][0]
        for player,card in self.currentHand[1:]:
            if maxCard.SUIT == card.SUIT or card.SUIT == self.drum:
                if maxCard < card:
                    maxCard = card
                    winningPlayer = player
        return winningPlayer

    #seperate the try into a seperate function and redo the logic above it :)
    def playerCall(self):
        currentMinCall = 14
        currWinner = self.turnOrder[0]
        for player in self.turnOrder:
            while call<28:
                try:
                    print(player.hand)
                    call = int(input(f"Player {player.id} please call(0 to pass)"))
                    if call == 0:
                        break
                    if call < currentMinCall or call > 28:
                        print(f"your call must be an integer between {currentMinCall}-28")
                        assert("Invalid choice")
                    currentMinCall = call+1
                    currWinner = player
                    break
                except Exception as e:
                    print(e)   
            
        return (currWinner,currentMinCall)
            

    def cardSelect(self,player:Player) -> Card:
        while True:
            try:
                print(player.hand)
                choice = int(input("Please enter the index of the card you want to choose(1 indexed)"))
                if choice < 1 or choice > len(player.hand):
                    assert("Invalid choice")
                return player.hand.pop(choice)
            except Exception as e:
                print(e)
            