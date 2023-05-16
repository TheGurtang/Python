class user():
    def logged_in(self):
      print('You have logged in')
    
class warden(user):
    def __init__(self, name, age, specification, weapon, strength):
      self.name = name
      self.age = age
      self.specification = specification
      self.weapon = weapon
      self.strength = strength

    def attack(self):
      print(f'The warden is attacking with: {self.strength}')

class witch():
    def __init__(self, name, age, specification, weapon, magic_power):
      self.name = name
      self.age = age
      self.specification = specification
      self.weapon = weapon
      self.magic_power = magic_power  

    def attack(self):
        print(f'Morrigen is spelling with her {self.magic_power}')

warden_1 = warden('Roman', 22, 'Swordsman', 'Dual daggers', 37 )
print('The grey Warden: ', warden_1.name, '\n He is', warden_1.age, 'years old', '\n He is an experienced ', warden_1.specification, '\n At the moment you are using ', warden_1.weapon, '\n His current strength is ', warden_1.strength)
warden_1.attack()

def warden_attack_checker(warden_1):
  while warden_1.strength >= 70:
      print('The warden is causing 40% of damage')
      break
  else:
      print('The warden is causing 20% of damage')
warden_attack_checker(warden_1)

witch_1 = witch('Morrigan', 25, 'Witch of the Wilds', 'Magic coal stuff', 74)
print('The wardens ally: ', witch_1.name, '\n She is', witch_1.age, 'years old', '\n She is an experienced ', witch_1.specification, '\n At the moment she is using ', witch_1.weapon, '\n her current power of magic is ', witch_1.magic_power)
witch_1.attack()
def witch_spell_checker(witch_1):
    while witch_1.magic_power >= 60:
        print('Morrigan hurts enemies with 40% of damage')
        break
    else:
        print('Morrigan hurts enemies with 20% of damage')
witch_spell_checker(witch_1)


def player_attack(char):           ### Here is polymorhism principle is exercised! We create a new function and assign a ner attribute 'char' for assigning the function which is COMMON for the both CLASSES and then we can run this function for the both classes
    char.attack()
player_attack(warden_1)
player_attack(witch_1)
                               ## However there is another way how to achieve this result
for char in [warden_1, witch_1]:   ##  we get the same result
    char.attack()

