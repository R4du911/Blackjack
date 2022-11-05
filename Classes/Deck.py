from random import randint

from Classes.AceCard import AceCard
from Classes.FaceCard import FaceCard
from Classes.Karte import Karte

class Deck:
    def __init__(self):
        self.deck = []

    def mischenKarten(self):
        for el in self.deck:
            index1 = randint(0,51)
            index2 = randint(0,51)
            self.deck[index1],self.deck[index2] = self.deck[index2], self.deck[index1]

    def get_nachste_Karte(self,index):
        return self.deck[index+1], index+1

    def get_deck(self):
        cards = [chr(code) for code in range(ord('🂡'), ord('🃞') + 1)]
        cards = [code for code in cards if code not in ['🂬', '🃀', '🃏', '🂿', '🂼', '🃌', '🃐', '🃜', '\U0001f0af', '\U0001f0b0']]
        elements = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        symbols = ['inima neagra', 'inima rosie', 'romb', 'trefla']
        indexel = 0
        indexsym = 0
        for el in cards:
            if indexel == 13:
                indexel = 0
                indexsym += 1
            if indexel == 0:
                card = AceCard(el,elements[indexel],symbols[indexsym])
                self.deck.append(card)
            elif indexel >= 10:
                card = FaceCard(el,elements[indexel],symbols[indexsym])
                self.deck.append(card)
            else:
                card = Karte(el,elements[indexel],symbols[indexsym])
                self.deck.append(card)
            indexel += 1
        self.mischenKarten()

