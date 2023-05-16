class Play_Character:
    def __init__(self, name, age, exp, weapon, armor):
        self.name = name
        self.age = age
        self.exp = exp
        self.weapon = weapon
        self.armor = armor

    @classmethod                          ## here the decorator comes
    def add_things(cls, num1, num2):      ##  here 'cls' is introduced to invoke on  'classa'
        return num1 + num2                ##  here  we show what particular action to perform

weapon = {
    'a': 'Handgun',
    'b': 'Assault rifle',
    'c': 'Sniper rifle'
}
armor = {
    'a': 'Scout armor',
    'b': 'Battle armor',
    'c': 'Assault armor'
}

player_1 = Play_Character('Miranda', 32, '13th level', input('Chose the weapon for Miranda: (a,b,c) '), input('Chose the armor for Miranda: (a,b,c) '))
print(player_1.name, player_1.age, player_1.exp, player_1.add_things(2,3))

def Miranda_weapon():
 if player_1.weapon == 'a':
     print(weapon.get('a'))
 elif player_1.weapon  == 'b':
     print(weapon.get('b'))
 elif player_1.weapon  == 'c':
     print(weapon.get('c'))
 else:
     print('You have not chosen the weapon!')
Miranda_weapon()

def Miranda_armor():
    if player_1.armor == 'a':
        print(armor.get('a'))
    elif player_1.armor == 'b':
        print(armor.get('b'))
    elif player_1.armor == 'c':
        print(armor.get('c'))
    else:
        print('You have not chosen the armor!')
Miranda_armor()

def Miranda_age_checker():
 if player_1.age < 29:
     print('That can not be Miranda!' )
 elif player_1.age > 35:
     print('That is not Miranda')
 else:
     print('Miranda Lawsome')
Miranda_age_checker()

player_2 = Play_Character('Shepard', 35, '9th level', input('Chose the weapon for Shepard: (a,b,c) '), input('Chose the armor for Shepard: (a,b,c)' ))
print(player_2.name, player_2.age, player_2.exp)
def Shepard_weapon():
 if player_2.weapon == 'a':
     print(weapon.get('a'))
 elif player_2.weapon  == 'b':
     print(weapon.get('b'))
 elif player_2.weapon  == 'c':
     print(weapon.get('c'))
 else:
     print('You have not chosen the weapon!')
Shepard_weapon()

def Shepard_armor():
    if player_2.armor == 'a':
        print(armor.get('a'))
    elif player_2.armor == 'b':
        print(armor.get('b'))
    elif player_2.armor == 'c':
        print(armor.get('c'))
    else:
        print('You have not chosen the armor!')
Shepard_armor()

def Shepard_age_checker():
    if player_2.age > 35:
        print('Shepard should not be older 35 years!')
    elif player_2.age <30:
        print('Shepard should not be younger 30 years!')
    else:
        print('That is Captain Shepard')
Shepard_age_checker()



