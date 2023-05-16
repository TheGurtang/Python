# Here we create our 'old-good' game with guessing random numbers

def the_game_intro():
    intro = input('Would you like to play this game? (yes\no): ')
    if intro == 'yes':
        import random
        n_num = random.randint(1,10)
        print(n_num)
        while True:
            guess = input('So, guess any number from 1 to 10: ')
            if 0 < int(guess) and int(guess) == n_num:
                print('Right you are!! You have guessed correct number!')
                break
            else:
                print('You are wrong! Try one more time!')
                continue
    else:
        print('Wi will be glad to see you later!')
print(the_game_intro())
