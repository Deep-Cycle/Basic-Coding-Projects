# Developer: Shen Z.
# Time: 2023-05-12 9:28 p.m.

import time
import random

start_message = '''
Thank you for playing this game.
Now, let\'s start the game.
This is a game about guessing the number.
The number is an integer between 0 and 100.
You only have 10 chances.
Enjoy your game, I wish you the best luck. 
          '''


def speaking(message):
    for char in message:
        print(char, end='')
        time.sleep(.03)


speaking(start_message)


while True:

    ans = random.randint(0, 100)

    i = 10
    while i > 0:
        i = i-1
        gue = input('\nPlease type in your guess of the number:')
        if gue.isnumeric() is True:
            gue = int(gue)
            if 0 <= gue <= 100:
                if gue > ans:
                    speaking('The answer is too big, you still have ' + str(i) + ' tries left.')
                    if i == 0:
                        speaking('The correct answer is ' + str(ans) + '.')
                        pass
                elif gue < ans:
                    speaking('The answer is too small, you still have ' + str(i) + ' tries left.')
                    if i == 0:
                        speaking('The correct answer is ' + str(ans) + '.')
                        pass
                else:
                    speaking('Congratulation, you got it!! \nThe number is ' + str(ans) + '.')
                    break
            else:
                speaking('Hint: the number is an integer in between 0 and 100.\nYou still have ' + str(i)
                         + ' tries left.')
        else:
            i = i + 1
            speaking('Please type in the number only.\nYou still have ' + str(i) + ' tries left')
    play_again = input('\nDo you want to play again? (y/n): ')
    if play_again.lower() != 'y':
        break
