#### Here we create 'random number game' in one function

def game():
    a = input('Would you like to play this game? (yes\no): ')
    if a == 'yes':
        import random
        outcome = random.randint(1,10)
        print(outcome)
        while True:
            gues = input('Chose the number between 1 and 10: ')
            if 0 < int(gues) < 11 and int(gues) == outcome:
                print('Right you are! You have fund the correct number!')
                break
            else:
                print('Wrong you are! Try one more time!')
                continue
    else:
        print('So sorry! Visit us later!')
print(game())

