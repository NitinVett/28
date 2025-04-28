from Player import Player
from CardEssentials import TYPE,SUIT
from Card import Card
import random as rand
class CardManager:
    
    # initializes full deck
    def __init__(self):
        self.deck = []
        self.resetDeck()

    # For all players in the list given it will deal 4 unique cards from the deck
    def dealCards(self,playerList:list[Player]) -> None:
        for player in playerList:
            for _ in range(4):
                # Generates a random index within the length of our deck array
                randomCardIndex = rand.randint(0,len(self.deck)-1)
                player.addCard(self.deck.pop(randomCardIndex))

    # Resets the deck to have all cards 7-Ace of each suit
    def resetDeck(self) -> None:
        self.deck = []
        
        CARDTYPES = [TYPE.ACE,TYPE.EIGHT,TYPE.JACK,TYPE.KING,TYPE.NINE,TYPE.QUEEN,TYPE.SEVEN,TYPE.TEN]
        CARDSUITS = [SUIT.CLUBS,SUIT.DIAMONDS,SUIT.HEARTS,SUIT.SPADES]

        for ctype in CARDTYPES:
            for suit in CARDSUITS:
                self.deck.append(Card(suit,ctype))