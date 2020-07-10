# guess the number game
from random import randint

def Game():
    """Core game mechanic."""
    rnd_num = randint(1, 100)
    while True:
        num = int(input('Enter a number between 1 and 100: '))
        if num > rnd_num:
            print('Too Big.')
        elif num < rnd_num:
            print('Too Small.')
        elif num == rnd_num:
            print('You guessed the number!')
            break
        else:
            print('Wrong input.')

def main():
    print('Guess the Number!')
    while True:
        usr_inp = input('Do you want to play a game? [y/n] - ')
        if usr_inp == 'n':
            print('Quiting...')
            break
        elif usr_inp == 'y':
            Game()

if __name__ == '__main__':
    main()
