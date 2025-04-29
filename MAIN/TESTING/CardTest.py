from ..CODE.Card import Card
from ..CODE.CardEssentials import *
import unittest


class CardTest(unittest.TestCase):
    
    
    def testComparison(self) -> None:
        # Test less than
        self.assertLess(Card(SUIT.HEARTS,TYPE.KING), Card(SUIT.SPADES,TYPE.ACE), "King should be less than Ace")
        self.assertLess(Card(SUIT.CLUBS,TYPE.QUEEN), Card(SUIT.HEARTS,TYPE.KING), "Queen should be less than King")
        
        # Test greater than
        self.assertGreater(Card(SUIT.SPADES,TYPE.ACE), Card(SUIT.HEARTS,TYPE.KING), "Ace should be greater than King")
        self.assertGreater(Card(SUIT.DIAMONDS,TYPE.JACK), Card(SUIT.SPADES,TYPE.TEN), "Jack should be greater than 10")
        
        # Test less than or equal
        self.assertLessEqual(Card(SUIT.SPADES,TYPE.KING), Card(SUIT.HEARTS,TYPE.KING), "Same card types with different suits should be equal")
        self.assertGreaterEqual(Card(SUIT.SPADES,TYPE.ACE), Card(SUIT.SPADES,TYPE.ACE), "Same cards should be equal")
    
    
    
    
    def run(self) -> None:
        self.testComparison()
        
