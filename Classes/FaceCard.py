from Classes.Karte import Karte

class FaceCard(Karte):
    def __init__(self,bild,rang,anzug):
        super().__init__(bild,rang,anzug)
        self.weichWert = 10
        self.hartWert = 10

    def __str__(self):
        return f'{self.bild}, {self.rang}, {self.anzug}'