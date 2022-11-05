from Classes.Deck import Deck

class Dealer:
    def __init__(self,deck) -> None:
        self.deck = deck

    def getNewCard(self,index):
        return self.deck.get_nachste_Karte(index)

    def getNewDeck(self):
        self.deck = Deck()