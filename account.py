class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r')as file:
            self.balance = int(file.read())


    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def perform(self):
        with open(self.filepath, 'w')as file:
            file.write(str(self.balance))


class Account_2(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount

account_2 = Account_2('balance.txt', 3)
print(account_2.balance)
account_2.transfer(33)
print(account_2.balance)






















#account = Account('balance.txt')
#print(account.balance)
#account.withdraw(250)
#print(account.balance)
#account.perform()
#account.deposit(35)
#account.perform()
#print(account.balance)

