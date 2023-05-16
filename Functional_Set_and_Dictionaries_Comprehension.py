## here we create a standart function for a list

def pick_num(lis):
    lis_2 = []
    for item in lis:
        lis_2.append((item+2) / 2)             ## here we creat an instruction of this function
    return lis_2
print(pick_num([8,12,45,67,34]))               ## here we have the function executiom

## Here we create list-comprehension method

lis_3 = [8,12,45,67,34]
lis_4 = [(item+2)/2 for item in lis_3]     ## here we introduce an instruction for the fucntion-comprehension
print(lis_4)

##  Here we create a standart function with set{}

def take_right(set):
    for item in set:
        if item >= 33:                     ##  here we insert instruction for the function
            print(item)
print(take_right({8,12,45,67,34}))


## Here we create set-comprehension method

set_1 ={8,12,45,67,34}
set_2 = {item for item in set_1 if item >= 20}              ##  here we introduce an instruction for a set-comprehension
print(set_2)

##  Here we create a standart function with a dictionary

dict = {'a':25, 'b':50, 'c':77}
def get_from_dict(dict):
    for item in dict:
        if item >= 33:
            get(dict(item))
print(get_from_dict)

##  Here we create dictionary-comprehension
dict_3 = {'a':25, 'b':50, 'c':77}
dict_4 = {keys:values*2 for keys,values in dict_3.items()}       ##  here we introduce an instruction for a dictionary-comprehension
##    pay attention to  "key$value" attribution, and "items()" function
print(dict_4)

##  Here we use LAMBDA with MAP, FILTER and ZIP  functions
add_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
ex_list = [12,25,48,97,53,19,93,64]
print(list(filter(lambda item: item %2 ==0, ex_list)))
print(list(filter(lambda item: item %2 !=0, ex_list)))
print(list(map(lambda item: (item+5)*2, ex_list)))
print(set(zip(add_list, ex_list)))

## Duplicate exercise

letters = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
letters_2 = []
for value in letters:
    if letters.count(value) > 1:             ##  It is the way we solve this task by means of a standard  function
        if value not in letters_2:
            letters_2.append(value)
print(letters_2)


letters_3 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
letters_4 = list(set([value for value in letters_3 if letters_3.count(value) > 1]))      ### it is the decision by means of comprehension method
print(letters_4)


weapon_1 = ['knife', 'gun', 'rifle', 'gun', 'granade', 'knife', 'landmine']
sorted = []
for item in weapon_1:
    if weapon_1.count(item) > 1:
        if item not in sorted:
            sorted.append(item)
print(sorted)

sorted_wp = list(set([item for item in weapon_1 if weapon_1.count(item) > 1]))
print(sorted_wp)



