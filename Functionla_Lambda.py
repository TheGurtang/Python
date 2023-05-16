def make_it_twice(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list
print(make_it_twice([22,44,77]))               ## It is example where we create an ordinarey function for one particular action (multiplying list by 2)

##  lambda-function is an unknown function which allows us to call the action WITHOUT creating a function, but only for ONE execution of an action

list_2 = [55,77,100]
print(list(map(lambda item:item * 2, list_2)))   ##  here we create lambda-function to execute ONE multiplication on 2

list_3 = [12,24,56,39,32,41,83,91,22,34,75]
print(list(filter(lambda item:item %2 != 0, list_3)))   ## here we created lambda for filtering list_3 for odds and even numbers respectively
print(list(filter(lambda item:item %2 == 0, list_3)))    ##  it is filtering for even numbers


list_4 = [5,4,3]
print(list(map(lambda item:item * item, list_4)))

list_5 = [(23,45), (32,18), (123,67), (13, -4)]
print(list_5.sort(key = lambda item:item[1]))
print(list_5)

list_5 = [(0,2), (4,3), (9,9), (10, -1)]
list_5.sort(key = lambda x:x[1])
print(list_5)


