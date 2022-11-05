from Classes.FaceCard import FaceCard

class AceCard(FaceCard):
    def __init__(self,bild,rang,anzug):
        super().__init__(bild,rang,anzug)
        self.weichWert = 1
        self.hartWert = 11

    def __str__(self):
        return f'{self.bild}, {self.rang}, {self.anzug}'