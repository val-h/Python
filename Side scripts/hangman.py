# HangMan game
from random import choice
from termcolor import colored

words = [
    'geese','penitent','untidy','fade','collar','likeable','son',
    'doubtful','shoes','check','weak','overflow','learned','glistening',
    'laugh','underwear','race','flood','can','internal','gaping','sand',
    'care','bit','cats',]

def Game():
    """The game mechanics."""
    word = choice(words)
    masked = ['_' for i in range(len(word))]
    tries = 9
    while tries > 0:
        print(f'You have {tries} tries...')

        # Display string for the console
        dis_str = '\t'
        for c in masked:
            dis_str += f'{c} '
        print(f'Word: {dis_str}')
        
        char = input('Enter a single char: ').lower()
        if len(char) == 1:
            found = False
            for i, c in enumerate(word):
                if char == c:
                   masked[i] = char
                   found = True
                   print('You guessed a charecter.') 
            # If the char was not guessed
            if found == False:
                tries -= 1
                print('Wrong answer.')
        else:
            print('Wrong input! Try again.')
        if '_' not in masked:
            print(colored('\nCongratulations! You won the game.', "green"))
            print(f'The word was: {colored(word, "yellow")}')
            break
        if tries == 0:
            print(colored('\nGame Over!', "red"))
            print(f'The word was: {colored(word, "yellow")}')
            break

def main():
    print(' --- HangMan Game ---')
    while True:
        usr_inp = input('Do you want to play a game? [y/n] - ')
        if usr_inp == 'y':
            Game()
        elif usr_inp == 'n':
            print('Quiting...')
            break
        else:
            print('Worng Input!')

if __name__ == '__main__':
    main()
