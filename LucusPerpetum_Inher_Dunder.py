class user():
    print('You have logged In!')

char = {
    'a': 'Samson',
    'b': 'Sharlei',
    'c': 'Rainevan'
}
print(char)
weapon = {
    'a': 'Hammer',
    'b': 'Sword and Dagger',
    'c': 'Handgun'
}
class fighter(user):
    def __init__(self, name,  level, skill):
        self.name = name
        self.level = level
        self.skill = skill
        self.weapon = {
            'a': 'Hammer',
            'b': 'Sword and Dagger',
            'c': 'Handgun'
        }
    def character(self):
        char_pic =input('Chose your character (a,b,c): ')
        if char_pic == 'a':
            print('You have chosen a mysterious warrior ', char.get('a'), self.level, self.skill)
        elif char_pic == 'b':
            print('You have chosen a dexterious fighter ', char.get('b'),  self.level, self.skill)
        elif char_pic == 'c':
            print('You have chosen a romantic healer ', char.get('c'), self.level, self.skill)
        else:
            print('You have not chosen any character!')
    def attack_checker(self):
        if self.level >= 17 and self.skill >= 30:
            print(f'{self.name} is attacking his opponent at 50% of damage!')
        elif self.level >= 10 and self.skill >= 20:
            print(f'{self.name} is attacking his opponent at 30% of damage!')
        elif self.level >= 5 and self.skill >= 10:
            print(f'{self.name} is attacking his opponent at 10% of damage!')
        else:
            print(f'{self.name} is uncapable of causing any damage!')

    def __getitem__(self, i):
        return print(f'{self.name} has ', weapon.get(i))
    def skill_checker(self):
       while self.skill >= 20:
           print(f'{self.name} is a skillful character!')
           break
       else:
           print(f'{self.name} still has what to learn!')

class rouge(user):
    def __init__(self, name,  level, skill):
        self.name = name
        self.level = level
        self.skill = skill
        self.weapon = {
            'a': 'Hammer',
            'b': 'Sword and Dagger',
            'c': 'Handgun'
        }
    def character(self):
        char_pic = input('Chose your character (a,b,c): ')
        if char_pic == 'a':
            print('You have chosen a mysterious warrior ', char.get('a'), self.level, self.skill)
        elif char_pic == 'b':
            print('You have chosen a dexterious fighter ', char.get('b'), self.level, self.skill)
        elif char_pic == 'c':
            print('You have chosen a romantic healer ', char.get('c'), self.level, self.skill)
        else:
            print('You have not chosen any character!')
    def attack_checker(self):
        if self.level >= 17 and self.skill >= 30:
            print(f'{self.name} is attacking his opponent at 50% of damage!')
        elif self.level >= 10 and self.skill >= 20:
            print(f'{self.name} is attacking his opponent at 30% of damage!')
        elif self.level >= 5 and self.skill >= 10:
            print(f'{self.name} is attacking his opponent at 10% of damage!')
        else:
            print(f'{self.name} is uncapable of causing any damage!')
    def __getitem__(self, i):
        return print(f'{self.name} has ', weapon.get(i))
    def skill_checker(self):
       while self.skill >= 20:
           print(f'{self.name} is a skillful character!')
           break
       else:
           print(f'{self.name} still has what to learn!')

class healer(user):
    def __init__(self, name, level, skill):
        self.name = name
        self.level = level
        self.skill = skill
        self.weapon = {
            'a': 'Hammer',
            'b': 'Sword and Dagger',
            'c': 'Handgun'
        }
    def skill_checker(self):
       while self.skill >= 20:
           print(f'{self.name} is a skillful character!')
           break
       else:
           print(f'{self.name} still has what to learn!')
    def character(self):
        char_pic = input('Chose your character (a,b,c): ')
        if char_pic == 'a':
            print('You have chosen a mysterious warrior ', char.get('a'),  self.level, self.skill)
        elif char_pic == 'b':
            print('You have chosen a dexterious fighter ', char.get('b'),  self.level, self.skill)
        elif char_pic == 'c':
            print('You have chosen a romantic healer ', char.get('c'),  self.level, self.skill)
        else:
            print('You have not chosen any character!')
    def attack_checker(self):
        if self.level >= 17 and self.skill >= 30:
            print(f'{self.name} is attacking his opponent at 50% of damage!')
        elif self.level >= 10 and self.skill >= 20:
            print(f'{self.name} is attacking his opponent at 30% of damage!')
        elif self.level >= 5 and self.skill >= 10:
            print(f'{self.name} is attacking his opponent at 10% of damage!')
        else:
            print(f'{self.name} is uncapable of causing any damage!')
    def __getitem__(self, i):
        return print(f'{self.name} has ', weapon.get(i))

    def skill_checker(self):
       while self.skill >= 20:
           print(f'{self.name} is a skillful character!')
           break
       else:
           print(f'{self.name} still has what to learn!')

class uni_char(fighter, rouge, healer):             ## here we created a new class which inherits all the previously created classes
    def __init__(self, name, level, skill):
        fighter.__init__(self, name, level, skill)
        rouge.__init__(self, name, level,  skill)
        healer.__init__(self, name, level, skill)

fighter_1 = fighter('Samson', 21, 35)
print(fighter_1.character())
print(fighter_1['a'])
print('\n He is a powerful warrior', '\n His level is ', fighter_1.level, '\n ', fighter_1.name, 'has his skills at', fighter_1.skill )

rouge_1 = rouge( 'Sharlei', 18, 23)
print(rouge_1.character())
print(rouge_1['b'])
print('\n He is a dexterious fighter!', '\n His level is ', rouge_1.level, '\n ', rouge_1.name, 'has his skills at', rouge_1.skill )

healer_1 = healer('Reinevan', 11, 13)
print(healer_1.character())
print(healer_1['c'])
print('\n He is a talanted healer!', '\n His level is ', healer_1.level, '\n ', healer_1.name, 'has his skills at', healer_1.skill )

uni_char_1 = uni_char('Urban Horn', 16, 23)


for att in [fighter_1, rouge_1, healer_1, uni_char_1]:
    att.attack_checker()

for att in [fighter_1, rouge_1, healer_1, uni_char_1]:
    att.skill_checker()