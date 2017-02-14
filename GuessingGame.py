import random

#FUNCTION
def game():
    g = random.randint(1, 4)

    answer = int(input('Guess the number, 1-4: '))
    if answer is g:
        print('You won one million dollars!')
    else:
        print('You lose')
    answer1 = str(input('To play again press Y: '))
    if answer1 is not 'Y':
        print('Goodbye')
    else:
        game()

#RUNNING THE FUNCTION
print("*** GUESS TO WIN THE GAME ***")
game()