class user():
    print('You are logged in!')

character = {
    'a': 'Diego',
    'b': 'General Lee',
    'c': 'Milten'
}
print(character)
weaponry = {
	'a':'sword',
	'b':'bow',
	'c':'stuff'
}
print(weaponry)
maps = {
    'a': 'Minenteil',
    'b': 'Chorinis',
    'c': 'Myrtana'
}
print(maps)


class archer(user):
    def __init__(self, name, exp_level, skill):
      self.name = name
      self.exp_level = exp_level
      self.skill = skill
      self.character = {
    'a': 'Diego',
    'b': 'General Lee',
    'c': 'Milten'
}
    def weapon(self):
      weap_pick = input('Chose the weapon for your character (a,b,c): ')
      if weap_pick == 'a':
        print(self.name, 'is armed with', weaponry.get('a'))
      elif weap_pick == 'b':
        print(self.name, 'is armed with', weaponry.get('b'))
      elif weap_pick == 'c':
        print(self.name, 'is armed with', weaponry.get('c'))
    def attack(self):
        print(f'{self.name} is attacking the enemy at {self.skill} ')
    def attack_checker(self):
        if self.skill >= 90:
            print(self.name, 'is causing 40% of damage')
        elif self.skill >= 45:
            print(self.name, 'is causing 20% of damage')
        else:
            print(self.name, 'has to improve his fighting skills!')
    def get_maps(self):
        pick_map = input(f'{self.name} should chose the way to go (a,b,c): ')
        if pick_map == 'a':
            print(f'{self.name} has gone to ', maps.get('a'))
        elif pick_map == 'b':
            print(f'{self.name} has gone to ', maps.get('b'))
        elif pick_map == 'c':
            print(f'{self.name} has gone to ', maps.get('c'))
        else:
            print(f'{self.name} must choose the way to embark upon!')


    def __getitem__(self, i):
        return print('You have chosen the character: ', self.character[i])


class warrior(user):
    def __init__(self, name, exp_level, skill):
        self.name = name
        self.exp_level = exp_level
        self.skill = skill
    def weapon(self):
      weap_pick = input('Chose the weapon for your character (a,b,c): ')
      if weap_pick == 'a':
        print(self.name, 'is armed with', weaponry.get('a'))
      elif weap_pick == 'b':
        print(self.name, 'is armed with', weaponry.get('b'))
      elif weap_pick == 'c':
        print(self.name, 'is armed with', weaponry.get('c'))
    def attack(self):
        print(f'{self.name} is attacking the enemy at {self.skill} ')
    def attack_checker(self):
        if self.skill >= 90:
            print(self.name, 'is causing 40% of damage')
        elif self.skill >= 45:
            print(self.name, 'is causing 20% of damage')
        else:
            print(self.name, 'has to improve his fighting skills!')
    def get_maps(self):
        pick_map = input(f'{self.name} should chose the way to go (a,b,c): ')
        if pick_map == 'a':
            print(f'{self.name} has gone to ', maps.get('a'))
        elif pick_map == 'b':
            print(f'{self.name} has gone to ', maps.get('b'))
        elif pick_map == 'c':
            print(f'{self.name} has gone to ', maps.get('c'))
        else:
            print(f'{self.name} must choose the way to embark upon!')

class wizard(user):
    def __init__(self, name, exp_level, skill):
        self.name = name
        self.exp_level = exp_level
        self.skill = skill
    def weapon(self):
      weap_pick = input('Chose the weapon for your character (a,b,c): ')
      if weap_pick == 'a':
        print(self.name, 'is armed with', weaponry.get('a'))
      elif weap_pick == 'b':
        print(self.name, 'is armed with', weaponry.get('b'))
      elif weap_pick == 'c':
        print(self.name, 'is armed with', weaponry.get('c'))
    def attack(self):
        print(f'{self.name} is attacking the enemy at {self.skill} ')
    def attack_checker(self):
        if self.skill >= 90:
            print(self.name, 'is causing 40% of damage')
        elif self.skill >= 45:
            print(self.name, 'is causing 20% of damage')
        else:
            print(self.name, 'has to improve his fighting skills!')
    def get_maps(self):
        pick_map = input(f'{self.name} should chose the way to go (a,b,c): ')
        if pick_map == 'a':
            print(f'{self.name} has gone to ', maps.get('a'))
        elif pick_map == 'b':
            print(f'{self.name} has gone to ', maps.get('b'))
        elif pick_map == 'c':
            print(f'{self.name} has gone to ', maps.get('c'))
        else:
            print(f'{self.name} must choose the way to embark upon!')



archer_1 = archer('Diego', 9, 45 )
print(archer_1['b'])
print('Your character is ', archer_1.name, '\n ', archer_1.name, 'is currently at level', archer_1.exp_level, '\n', archer_1.name, 'has his', archer_1.skill,'of dexterity' )
archer_1.weapon()


warrior_1 = warrior('General Lee', 15, 110)
print('Your character is', warrior_1.name, '\n ', warrior_1.name, 'is currently at level', warrior_1.exp_level, '\n', warrior_1.name, 'has his', warrior_1.skill, 'of power' )
warrior_1.weapon()

wizard_1 = wizard('Milten', 11, 80)
print('Your character is', wizard_1.name, '\n ', wizard_1.name, 'is currently at level', wizard_1.exp_level, '\n', wizard_1.name, 'has his', wizard_1.skill, 'of power')
wizard_1.weapon()

                      ##  here we created one function-call for all three classes
for char in [archer_1, warrior_1, wizard_1]:
    char.attack()
                      ##  here we created one function-call for all three classes
for char in [archer_1, warrior_1, wizard_1]:
    char.attack_checker()
                      ##  here we created one function-call for all three classes
for char in [archer_1, warrior_1, wizard_1]:
    char.get_maps()