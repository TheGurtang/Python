class user():
    def sign_in(self):
        print('You have logged in!')

class sorcerror(user):         ## we insert  class 'user' into another classes to INHERIT its property
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'Attacking with the power of  {self.power}')



class worrior(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'The worrior is attacking with his sword at power of {self.power} ')


class archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'Attacking with the arrows: arrows left -  {self.num_arrows} ')


class rogue(user):
    def __init__(self, name, dexterity):
        self.name = name
        self.dexterity = dexterity
    def attack(self):
        print(f'He is delivering a deadly stab with all his dexterity - {self.dexterity}')

sorcerror_1 = sorcerror('Xardas', 130)
print(sorcerror_1.sign_in())     ## here we assign our variable "sorcerror_1" to class 'sorcerror()' with all its properties
print(sorcerror_1.name, '\n His power is ', sorcerror_1.power)
sorcerror_1.attack()      ##  that is where we assign sorcerror_1  .attack() which is an inherited attribute now

archer_1 = archer('Rachir', 75)
print(archer_1.name, '\n He is carrying ', archer_1.num_arrows, 'arrows')
archer_1.attack()

worrior_1 = worrior('Elric of Melnibone', 110)
print(worrior_1.name, '\n He has power of', worrior_1.power)
worrior_1.attack()

rogue_1 = rogue('Lusien', 77)
print(rogue_1.name, '\n His dexterity equals to ', rogue_1.dexterity)
rogue_1.attack()