class Game():
    def __init__(self, game):
        self.gameName = game

    def __getGameName(self, game):
        print(type(game))
        self.gameName = self.gameName.lower()
        self.gameName = self.gameName.split()
        
    def output(self):
        self.__getGameName(self.gameName)

        return self.gameName