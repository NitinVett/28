
import unittest
from ..CODE.Player import Player
from ..CODE.CardManager import CardManager
class CardManagerTest(unittest.TestCase):
    
    def testCardCount(self,playerList:list[Player],manager:CardManager):
        for i in range(2):
            
            manager.dealCards(playerList)
            
            for player in playerList:
                self.assertEqual(len(player.hand),4*(i+1),"Players have been dealth incorrect number of cards")
        
            self.assertEqual(len(manager.deck),32-(16*(i+1)),"Dealer is not removing card from deck after it is dealt")

    def testUniqueCards(self,playerList:list[Player]):
        uCards = []

        for player in playerList:
            for card in player.hand:
                self.assertNotIn((card.TYPE,card.SUIT),uCards,"Duplicate cards found in player hands")

    
    def run(self):
        playerList = [Player(1),Player(2),Player(3),Player(4)]
        manager = CardManager()

        self.testCardCount(playerList,manager)
        self.testUniqueCards(playerList)






