list_1 = [123,23,127,18,23,56,123,87,18]
list_2 = []
for i in list_1:
    if list_1.count(i) > 1:
        list_2.append(i)
print(list(set(list_2)))

def new_list():
    list_3 = []
    for i in range(0,200, 13):
        list_3.append(i)
        print(list_3)
new_list()


print('new code!')
list_4 = []
for el in range(0, 77, 3):
    list_4.append(el)

print(list_4)

def multiply(elem):
    return elem *2
print(list(map(multiply, list_4)))


