



class Store:

    def __init__(self, StoreName, PreLink, RemoveSymbol):
        self.storeName = StoreName
        self.preliminaryLink = PreLink #Ссылка до обработки
        self.removeSymbolForLink = RemoveSymbol

    @staticmethod
    def GetGameName():
        print("Введите название игры: ")
        gameNameBeforeEditing = str(input())

        gameName = gameNameBeforeEditing.lower()
        gameName = gameName.strip()

        return gameName
