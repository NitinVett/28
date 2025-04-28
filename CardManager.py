from Player import Player
from CardEssentials import TYPE,SUIT
class CardManager:
    def __init__(self):
        self.deck = []
        cardTypes = [TYPE.ACE,TYPE.EIGHT,TYPE.JACK,TYPE.KING,TYPE.NINE,TYPE.QUEEN,TYPE.SEVEN,TYPE.TEN]
        cardSuits = [SUIT.CLUBS,SUIT.DIAMONDS,SUIT.HEARTS,SUIT.SPADES]

        for ctype in cardTypes:
            for suit in cardSuits:
                self.deck

    def dealCards(self,playerList:list[Player]) -> None:
        for player in playerList:
            player.

