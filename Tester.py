from Classes.Game import Game
from Classes.Deck import Deck
from Classes.Dealer import Dealer


def check_Kartentausch():
    deck1 = Deck()
    deck2 = Deck()
    deck1.get_deck()
    deck2.get_deck()

    assert deck1.deck is not deck2.deck


def check_Karte_einzigartig():
    deck = Deck()
    deck.get_deck()
    dealer = Dealer(deck)

    for index in range(len(deck.deck) - 1):
        card, index = dealer.getNewCard(index)
        for el in range(index + 1, len(deck.deck)):
            assert card != deck.deck[el]


def check_weich_hart_Wert():
    deck = Deck()
    deck.get_deck()
    for card in deck.deck:
        if card.rang in ['J','Q','K']:
            assert card.weichWert == card.hartWert == 10
        elif card.rang == 'A':
            assert card.weichWert == 1
            assert card.hartWert == 11
        else:
            assert card.weichWert == card.hartWert == card.rang

