from Classes.Dealer import Dealer
from Classes.Deck import Deck
from Classes.Nutzer import Nutzer
from Classes.Scores import Score, ScoresController
from datetime import datetime

class Game:
    def __init__(self) -> None:
        deck = Deck()
        deck.get_deck()
        self.dealer = Dealer(deck)

        name = input('Player Name: ')
        self.player = Nutzer(name)
        self.scoreController = ScoresController()


    def play(self):
        self.scoreController.sortScores()
        index_highscore = 1
        for score in self.scoreController.scores:
            print(f'#{index_highscore}  {score}')
            index_highscore += 1

        index_cards=-1
        roundsPlayed = 1

        while roundsPlayed <= 5:
            print(f'Round: {roundsPlayed}')
            index_cards = self.blackjack_round(index_cards)
            if self.player.dinero == 0:
                break
            else:
                roundsPlayed += 1

        #end of the game
        newScore = Score(datetime.now(), roundsPlayed-1, self.player.name, self.player.dinero)
        self.scoreController.addScore(newScore)

    def blackjack_round(self,index_cards):
        sum_wert = 0
        end = 0

        #Spieler
        #prima carte de la jucator
        print("Spieler:"+'\n')
        bet = int(input("Bet="))
        if bet > self.player.dinero or bet<0:
            print(f'Du bist nur mit: {self.player.dinero} Geld geblieben')
            bet = int(input("Bet="))
        if index_cards == 52:
            self.dealer.deck.get_deck()
            index_cards = -1
        card_spieler, index_cards = self.dealer.getNewCard(index_cards)
        if card_spieler.rang == 'A':
            sum_wert += self.ass_check()
        else:
            sum_wert += card_spieler.weichWert
        print(card_spieler)
        print(sum_wert)

        #urmatorele carti de la jucator pana jucatorul vrea sa se opreasca sau face 21 sau peste 21
        weiter = input("Mochtest du noch eine Karte:")
        while weiter == 'ja':
            if index_cards == 52:
                self.dealer.deck.get_deck()
                index_cards = -1
            card_spieler, index_cards = self.dealer.getNewCard(index_cards)
            if card_spieler.rang == 'A':
                sum_wert += self.ass_check()
            else:
                sum_wert += card_spieler.weichWert
            print(card_spieler)
            print(sum_wert)
            if sum_wert > 21:
                end = 1
                print("Du hast die Runde verloren")
                self.player.substractMoney(bet)
                break
            if sum_wert == 21:
                end = 1
                print("Du hast die Runde gewonnen")
                self.player.addMoney(bet)
                break
            weiter = input("Mochtest du noch eine Karte:")

        # Dealer
        # end = 1 => deja a castigat sau pierdut jucatorul, dealer-ul nu mai trebuie sa mai joace
        if end == 0:
            print('\n')
            print("Dealer:"+'\n')
            dealer_wert = 0
            while dealer_wert < 17:
                if index_cards == 52:
                    self.dealer.deck.get_deck()
                    index_cards = -1
                card_dealer, index_cards = self.dealer.getNewCard(index_cards)
                if card_dealer.rang == 'A':
                    if dealer_wert+card_dealer.hartWert == 21:
                        dealer_wert += card_dealer.hartWert
                else:
                    dealer_wert += card_dealer.weichWert
                print(card_dealer)
                print(dealer_wert)

            if dealer_wert > 21:
                self.player.addMoney(bet)
            elif sum_wert > dealer_wert:
                self.player.addMoney(bet)
            elif sum_wert < dealer_wert:
                self.player.substractMoney(bet)
        print(f'Gebliebenes Geld: {self.player.dinero}')
        print('\n')

        return index_cards

    def ass_check(self):
        wert = int(input("Mochtest du, dass 'A' den Wert 1 oder 11 hat?"))
        return wert