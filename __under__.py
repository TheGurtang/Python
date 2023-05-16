class user():
    def log_in():
        print('You have Logged In')

weapon_set = {
'a': 'Sword',
'b': 'Bow',
'c': 'Stuff'
}

location = {
'a': 'Darklands',
'b': 'Relinquin-akh',
'c': 'Tanalorn'
}


class warrior(user):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def weapon_pick(self):
        print(weapon_set)
        weap = input('Chose the weapon for your cahracter (a,b,c): ')
        if weap == 'a':
            print(self.name, 'have chosen the ', weapon_set.get('a'))
        elif weap == 'b':
            print(self.name, 'have chosen the ', weapon_set.get('b'), 'This weapon does not suit you!')
        elif weap == 'c':
            print(self.name, 'have chosen the ', weapon_set.get('c'), 'This weapon does not suit you!')
        else:
            print('There is no such weapon in our armory!')
    def attack_checker(self):
        if self.level >= 13:
            print(self.name, 'attacks the enemy with 20% of damage')
        elif self.level >= 7:
            print(self.name, 'attacks the enemy with 10% of damage')
        else:
            print(self.name, 'attacks the enemy with 5% of damage')
    def pick_way(self):
        print(location)
        way = input('Chose the way for your Heroes! (a,b,c): ')
        if way == 'a':
            print('Your way is leading to ', location.get('a'), 'prepare for numerous dangers!')
        elif way == 'b':
            print('Through the steaming ocean you will embark on ', location.get('b'), 'Be careful!')
        elif way == 'c':
            print('You are setting off the ', location.get('c'), 'which is only known about - being notexistant!')
        else:
            print('You can not stay here for eternity. Chose your way!')

class archer(user):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def weapon_pick(self):
        print(weapon_set)
        weap = input('Chose the weapon for your cahracter (a,b,c): ')
        if weap == 'a':
            print(self.name, 'have chosen the ', weapon_set.get('a'), 'This weapon does not suit you!')
        elif weap == 'b':
            print(self.name, 'have chosen the ', weapon_set.get('b'), 'That is your weapon!')
        elif weap == 'c':
            print(self.name, 'have chosen the ', weapon_set.get('c'), 'This weapon does not suit you!')
        else:
            print('There is no such weapon in our armory!')
    def attack_checker(self):
        if self.level >= 13:
            print(self.name, 'attacks the enemy with 20% of damage')
        elif self.level >= 7:
            print(self.name, 'attacks the enemy with 10% of damage')
        else:
            print(self.name, 'attacks the enemy with 5% of damage')
        def pick_way(self):
            print(location)
            way = input('Chose the way for your Heroes! (a,b,c): ')
        if way == 'a':
            print('Your way is leading to ', location.get('a'), 'prepare for numerous dangers!')
        elif way == 'b':
            print('Through the steaming ocean you will embark on ', location.get('b'), 'Be careful!')
        elif way == 'c':
            print('You are setting off the ', location.get('c'), 'which is only known about - being notexistant!')
        else:
            print('You can not stay here for eternity. Chose your way!')
    def pick_way(self):
        print(location)
        way = input('Chose the way for your Heroes! (a,b,c): ')
        if way == 'a':
            print('Your way is leading to ', location.get('a'), 'prepare for numerous dangers!')
        elif way == 'b':
            print('Through the steaming ocean you will embark on ', location.get('b'), 'Be careful!')
        elif way == 'c':
            print('You are setting off the ', location.get('c'), 'which is only known about - being notexistant!')
        else:
            print('You can not stay here for eternity. Chose your way!')

class wizard(user):
    def __init__(self, name, level):
        self.name = name
        self.level = level
    def weapon_pick(self):
        print(weapon_set)
        weap = input('Chose the weapon for your cahracter (a,b,c): ')
        if weap == 'a':
            print(self.name, 'have chosen the ', weapon_set.get('a'), 'This weapon does not suit you!')
        elif weap == 'b':
            print(self.name, 'have chosen the ', weapon_set.get('b'), 'This weapon does not suit you')
        elif weap == 'c':
            print(self.name, 'have chosen the ', weapon_set.get('c'), 'That is your weapon!')
        else:
            print('There is no such weapon in our armory!')
    def attack_checker(self):
        if self.level >= 13:
            print(self.name, 'attacks the enemy with 20% of damage')
        elif self.level >= 7:
            print(self.name, 'attacks the enemy with 10% of damage')
        else:
            print(self.name, 'attacks the enemy with 5% of damage')

        print(location)
        way = input('Chose the way for your Heroes! (a,b,c): ')
        if way == 'a':
            print('Your way is leading to ', location.get('a'), 'prepare for numerous dangers!')
        elif way == 'b':
            print('Through the steaming ocean you will embark on ', location.get('b'), 'Be careful!')
        elif way == 'c':
            print('You are setting off the ', location.get('c'), 'which is only known about - being notexistant!')
        else:
            print('You can not stay here for eternity. Chose your way!')
    def pick_way(self):
        print(location)
        way = input('Chose the way for your Heroes! (a,b,c): ')
        if way == 'a':
            print('Your way is leading to ', location.get('a'), 'prepare for numerous dangers!')
        elif way == 'b':
            print('Through the steaming ocean you will embark on ', location.get('b'), 'Be careful!')
        elif way == 'c':
            print('You are setting off the ', location.get('c'), 'which is only known about - being notexistant!')
        else:
            print('You can not stay here for eternity. Chose your way!')

warrior_1 = warrior('Elric', 11)
print('Your character is ', warrior_1.name, '\n', warrior_1.name, 'has', warrior_1.level, 'th level')
warrior_1.weapon_pick()
warrior_1.attack_checker()

archer_1 = archer('Rachir', 7)
print('Your character is ', archer_1.name, '\n', archer_1.name, 'has', archer_1.level, 'th level')
archer_1.weapon_pick()
archer_1.attack_checker()

wizard_1 = wizard('Corum', 6)
print('Your character is ', wizard_1.name, '\n', wizard_1.name, 'has', wizard_1.level, 'th level')
wizard_1.weapon_pick()
wizard_1.attack_checker()

warrior_1.pick_way()
