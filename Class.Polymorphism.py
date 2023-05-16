class user():
    print('You have logged in')

swords = {
    'a': 'Stornbringer',
    'b': 'Soulreaver',
    'c': 'Widowmaker'
}
stuffs = {
    'a': 'Carved stuff',
    'b': 'Winter breath',
    'c': 'Dragon heart'
}

class warrior(user):
    def __init__(self, name, level, weapon, strength):
        self.name = name
        self.level = level
        self.weapon = weapon
        self.strength = strength
    ## here we create an additional function for the class
    def attack(self):
        print(f'Using his {self.weapon}, {self.name} drains enemies souls with {self.strength}!')    ## this function has two ammendable, dynamic attributes from the previous function
    def weapon_pick(self):
        for swords_pick in swords:
            input('Kain is picking weapon (a,b,c): ')
        if swords_pick == 'a':
            print(self.name, 'has chosen', swords.get('a'))
        elif swords_pick == 'b':
            print(self.name, 'has chosen', swords.get('b'))
        elif swords_pick == 'c':
            print(self.name, 'has chosen', swords.get('c'))
        else:
            print(self.name, 'has not chosen any weapon!')


class wizard(user):
    def __init__(self, name, level, weapon, magic):
        self.name = name
        self.level = level
        self.weapon = weapon
        self.magic = magic
    def attack(self):
        print(f'Using his {self.weapon}, {self.name} destroys his enemies with {self.magic} !')
    def weapon_pick(self):
        for stuffs_pick in stuffs:
            input(f'{self.name} is picking weapon (a,b,c): ')
        if stuffs_pick == 'a':
            print(self.name, 'has chosen', stuffs.get('a'))
        elif stuffs_pick == 'b':
            print(self.name, 'has chosen', stuffs.get('b'))
        elif stuffs_pick == 'c':
            print(self.name, 'has chosen', stuffs.get('c'))
        else:
            print(self.name, 'has not chosen any stuff!')

warrior_1 = warrior('Nameless hero', 13, 'Urizel', 55)
print('Your character is ', warrior_1.name, 'His current level is ', warrior_1.level, '\n His weapon is ', warrior_1.weapon, ' and his strength is ', warrior_1.strength)
warrior_1.attack()
warrior_1.weapon_pick()


def Kain_attack_checker(warrior_1):
    while warrior_1.strength >= 50:
        print(warrior_1.name, 'attack is causing damage for 40% ')
        break
    else:
        print(warrior_1.name, 'attack is causing damage for 20% ')
Kain_attack_checker(warrior_1)

wizard_1 = wizard('Xardas', 13, 'Dragons heart', 45)
print('Your character is ', wizard_1.name, 'His current level is ', wizard_1.level, '\n His weapon is ', wizard_1.weapon, ' and his magic power is ', wizard_1.magic)
wizard_1.attack()
wizard_1.weapon_pick()

def Xardas_attack_checker(wizard_1):
    while wizard_1.magic >= 40:
        print(wizard_1.name, 'attack is causing damage for 40%')
        break
    else:
        print(wizard_1.name, 'attack is causing damage for 20%')
Xardas_attack_checker(wizard_1)
             ## Here we create a function which may launch the inherited function with one command
for char in [warrior_1, wizard_1]:
    char.attack()
               ## Here we create a function which may launch the inherited function with one command
for char_1 in [warrior_1, wizard_1]:
    char_1.weapon_pick()