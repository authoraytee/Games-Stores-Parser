from game import Game
from service import Service



if __name__ == "__main__":
    print('')
    print('Enter Q or Quit to exit')

    while(True):
        print('')
        gama = str(input("Enter a game: "))

        if gama.lower() == 'q' or gama.lower() == 'quit':
            print('Thanks for using!!!')
            break

        game = Game(gama).output()
        steampay = Service('https://steampay.com/game/', game, '-', 'div', 'product__current-price')
        print(steampay.output())
