from game import Game
from service import Service
import initialize_parser

def print_data(gama):
    game = Game(gama).output()
    parsed_data = initialize_parser.get_price(game)

    price = parsed_data['price']
    link = parsed_data['link']

    print('1.Epicgames: {}\n Link: {}'.format(price['epicgames'], link['epicgames']))
    print('-'*30)
    print('2.Playstationstore: {}\n Link: {}'.format(price['playstationstore'], link['playstationstore']))
    print('-'*30)
    print('3.Microsoftstore: {}\n Link: {}'.format(price['microsoftstore'], link['microsoftstore']))
    print('-'*30)
    print('4.Steam: {}\n Link: {}'.format(price['steam'], link['steam']))
    print('-'*30)
    print('5.Steampay: {}\n Link: {}'.format(price['steampay'], link['steampay']))
    print('-'*30)
    print('6.Gabestore: {}\n Link: {}'.format(price['gabestore'], link['gabestore']))
    print('-'*30)
    print('7.Icegames: {}\n Link: {}'.format(price['icegames'], link['icegames']))
    print('-'*30)
    print('8.Gamefarm: {}\n Link: {}'.format(price['gamefarm'], link['gamefarm']))
    print('-'*30)
    print('9.Epicgames: {}\n Link: {}'.format(price['epicgames'], link['epicgames']))
    print('-'*30)
    print('10.Steambuy: {}\n Link: {}'.format(price['steambuy'], link['steambuy']))



if __name__ == "__main__":
    print('')
    print('Enter Q or Quit to exit')

    while(True):
        print('')
        gama = str(input("Enter a game: "))

        if gama.lower() == 'q' or gama.lower() == 'quit':
            print('Thanks for using!!!')
            break

        print_data(gama)
