def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item * 2)
    return new_li
print(multiply_by2([4,6,8]))

                ##  supposing we would like to do it with a lighter, simpler code

                ##  map() comes up to help

def multiply_by2(item):
    return item * 2
print(list(map(multiply_by2, [4,6,8])))   ##   map() requires 2 arguments 1 - function (def ...) and 2 - value (list [])


                ## supposing we want to get the result FILTERED by a particular criteria
                ## filter() comes up helpful
nums = [12,24,56,39,32,41,83,91,22,34,75]
def odd_check(item):
    return item % 2 != 0
print(list(filter(odd_check, nums)))     ## here filter() has checked the list and returned only the values complying with the given criteria (%2 != 0)


                 ## supposing we want to ZIP two or more lists together
                 ## that is where zit() comes up helpful
peers = ['Roman', 'Samuel', 'Joshua', 'Cate', 'Xavier']
nums = [89655195982,89915793482,89122391942,87633121965,87553237865]
smun = ['fgevara@yandex.ru','sam182@yandex.ru','Jo_fan@yandex.ru','Kiity-Cat@yandex.ru','Professor@yandex.ru']

print(list(zip(peers, nums, smun)))            ## here we just put two lists together - creating a new data-structure, touples.  We may also put more than two lists together
