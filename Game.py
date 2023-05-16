import random

param_1 = random.randint(1,10)
print(param_1)

def game():
    while True:
        guess = input('Guess any number from 1 till 10: ')
        print('You have chosen ', guess)
        if 0 < int(guess) < 11 and int(guess) == param_1:
            print('Gongratulation!')
            break
        else:
            print('You are wrong! Try one more time!')
            continue
print(game())