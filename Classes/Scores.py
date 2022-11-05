import pickle

class Score:
    def __init__(self, date, roundsPlayed, name, dinero) -> None:
        self.date = date
        self.roundsPlayed = roundsPlayed
        self.name = name
        self.dinero = dinero

    def __str__(self):
        return f'{self.date}, {self.roundsPlayed}, {self.name}, {self.dinero}'

    __repr__ = __str__

class ScoresController:
    def __init__(self) -> None:
        self.__filePath = 'data/scores.txt'
        self.scores = self.getScores()

    def getScores(self):
        with open(self.__filePath, 'rb') as f:
            try:
                return pickle.load(f)
            except:
                return []

    def addScore(self, score):
        self.scores.append(score)
        self.__saveScores()

    def sortScores(self):
        return sorted(self.scores, key=lambda score: score.dinero, reverse=True)

    def __saveScores(self):
        with open(self.__filePath, 'wb') as f:
            pickle.dump(self.scores, f)

