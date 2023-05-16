## here we create a stupid game

import random

result = random.randint(1,10)
print(result)

def game():
    while True:
        gues = input('Please, insert your number brom 1 till 10: ')
        if 0 < int(gues) <11 and int(gues) == result:
            print('Right you are! Correct number!')
            return
        else:
            print('Wrong you are! Try once more!')
            continue
print(game())


