# here we create a plain function which is going to be subjected to testing

def do_stuff(num):
    return num + 5


def calcul():
    a = 'gurtang'
    b = a.capitalize()
    print(b)

def get_word():
    a = input('Insert your word: ')
    return a.capitalize()
    b == a


seq = 'There is an interesting text for working over'
def seq_n():
    seq_3 = []
    seq_2 = input('Insert the element: ')
    for i in seq_2:
        if i not in seq:
            seq_3.append(i)
    return seq_3
print(seq_n())


num = range(15,60,3)
def amply(num):
    num_1 = []
    for i in num:
        if i * 2 >100:
            num_1.append(i)
    return num_1
print(amply(num))
