class Karte:
    def __init__(self,bild,rang,anzug):
        self.bild = bild
        self.rang = rang
        self.anzug = anzug
        self.weichWert = rang
        self.hartWert = rang

    def __str__(self):
        return f'{self.bild}, {self.rang}, {self.anzug}'