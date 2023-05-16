class user():
    print('You have logged in!')


class knight(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.weaponry = {
            'a': 'Sword',
            'b': 'Lance',
            'c': 'Mace'
        }

    def char_attack(self):
        print(f'{self.name} is attacking with his {self.power}')

    def __getitem__(self, i):
        return print(f'Your {self.name} has a weapon: ', self.weaponry[i])


class deamon(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def char_attack(self):
        print(f'{self.name} is attacking with his {self.power}')

knight_1 = knight('Arthur', 33)
print('It is the well-known', knight_1.name, '\n He has power at ', knight_1.power)
print(knight_1['b'])

deamon_1 = deamon('Betrezen', 66)
print('It is the well-known', deamon_1.name, '\n He has power at ', deamon_1.power)

for charecters in [knight_1, deamon_1]:
    charecters.char_attack()