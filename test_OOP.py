class Test_1:

    def __init__(self, file):
        self.file = file
        with open('test.txt', 'r')as file_2:
            self.money = int(file_2.read())


    def take(self, amount):
        self.money = self.money - amount


    def put_int(self, amount):
        self.money = self.money + amount


    def write_in(self):
        with open(self.file, 'w')as file_3:
            file_3.write(str(self.money))


class Test_2(Test_1):

    def __init__(self, file, fee):
        Test_1.__init__(self, file)
        self.fee = fee

    def transfer(self, amount):
        self.money = self.money - amount


test_2 = Test_2('test.txt', 13)
print(test_2.money)
test_2.transfer(265)
print(test_2.money)







#test_1 = Test_1('test.txt')
#print(test_1.money)
#test_1.put_int(340)
#print(test_1.money)
#test_1.take(150)
#print(test_1.money)