def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
for s in fib(5):
    print(s)



print('Task1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.')

def find_num():
    got_figs=[]
    for i in range(20, 32):
        if i %7 ==0 and i%5 !=0:
            got_figs.append(i)
    return got_figs
print(find_num(), end=',')

print('the same task solved with generator and comprehension')
print(*(i for i in range(20, 32) if i%7==0 and i%5 !=0))    ## comprehension solution


print('Ефыл 2: Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program')

import math                                      ## here we import a special library which has a lot of specially designed math-fucntion
n = int(input('Insert your Factorial: '))
sol = math.factorial(n)                                ## here we implement the library, function(factorial() and our variable
print(sol)



print('Task 3: With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} ')

def make_dict():
    n = int(input('Please, insert your number: '))
    dict = {}
    for i in range(1,n*1):
        dict[i] = i * i
    print(dict)
make_dict()


print('Task 4: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program')

def seq():
    a = input('Insert your sequens of figures: ').split(',')     ## here we use "input().split(',')" to reate a console taking a sequence of figures separated by comma
    b = []
    for i in a:
        b.append(i)
    print(b, sep=',')
    tpl = tuple(b)                                                ##  here we use "touple()"-function for converting a list into a touple
    print(tpl)
seq()

print('Task 5: Define a class which has at least two methods: getString: to get a string from console input and printString: to print the string in upper case Also please include simple test function to test the class methods')
class my_class():
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def pic_str(self):
        a = str(input('Insert your text: '))
        print(a.upper())

my_class_1 = my_class('Collection', '01.03.2021')
print(my_class_1.name, '\m', my_class_1.date)
my_class_1.pic_str()


print('Task 6: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically ')
def words_line():
    a = input('Insert your text: ').split(',')
    b = sorted(a)
    print(b)
words_line()

print('Task 7: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized')
def get_lines():
    lst = []
    while True:
        a = input()
        if len(a)==0:
            break
        lst.append(a.upper())
    for line in lst:
        print(line)
get_lines()