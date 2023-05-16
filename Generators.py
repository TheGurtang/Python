def sel(num):
    odd_list=[]
    for item in range(num):
        if item %2 !=0:
            odd_list.append(item)
    return odd_list
print(sel(100))

print('Here a new range begins!')
list_3 = [item for item in range(5,55,3) if item %2 ==0]
print(list_3)

dict_1 = {'a':250, 'b': 350, 'c': 450}
dict_2 = {k:v for k,v in dict_1.items() if v >300}
print(dict_2)
dict_3 = (dict_1['c'] - dict_1['a']) + dict_1['b']
print(dict_3)

## generators with YIELD-trigger

def generatir_func(num):
    for i in range(num):
        yield i * 5        ##  here YIELD function creates the action (i *2) which will be exercised over and over again as long as we use commend NEXT

a = generatir_func(200)     ##  here we appoint veriable A
next(a)
next(a)
print(next(a))                ##  here we use NEXT command with the assigned veriable A to make each step of fucntion execution


## Suppose we create anothergenerator
print('New genertor starts here!')
def new_gen(num):
    for i in range(num):
        yield (i + 5)/2
b = new_gen(100)
next(b)
next(b)
next(b)
next(b)
print(next(b))

## Here we use Generator combined with __init__ function
print('THis is combined Generator')

