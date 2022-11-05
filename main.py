from Classes.Game import Game
from Tester import check_Kartentausch,check_Karte_einzigartig, check_weich_hart_Wert
from Classes.Scores import ScoresController

def main():
    check_Kartentausch()
    check_Karte_einzigartig()
    check_weich_hart_Wert()

    g = Game()
    g.play()



main()
