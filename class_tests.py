class PlayCharacter:
    def __init__(self, name, age, race, loialty):
        self.name = name
        if (age < 18):            ##   here we just try to introduce an additional condition to our code
            print('All characters should be older 18 years!' )
        elif (age > 40):
            print('All characters must not be older 40 years')
        else:
         self.age = age
        self.race = race
        self.loialty = loialty


player_1 = PlayCharacter(input('Chose the name of your character: ' ), int(input('Chose your characters age: ' )), input('Chose your race: ' ), input('Whom do you loyal? ' ))

print(player_1.name, player_1.age, player_1.race, player_1.loialty)



