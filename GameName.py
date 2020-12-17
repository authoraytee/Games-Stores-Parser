@staticmethod
def GetGameName():
    print("Введите название игры: ")
    gameNameBeforeEditing = str(input())

    gameName = gameNameBeforeEditing.lower()
    gameName = gameName.strip()

    return gameName
