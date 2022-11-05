class Nutzer:
    def __init__(self, name) -> None:
        self.name = name
        self.dinero = 100  # mereu un jucator incepe cu 100 de iepuroi

    def changeMoneyAmount(self,amount):
        self.dinero = amount

    def addMoney(self, amount):
        self.dinero += amount

    def substractMoney(self, amount):
        self.dinero -= amount