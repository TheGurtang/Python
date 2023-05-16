dict_1 = {'Hydrogen': 1, 'Oxygen':2}
print(dict_1)
thirdElement = dict_1.setdefault('Uran', 13)      ## .setdefault() inserts into a dictionary a new set of keys and values
print(dict_1)
dict_2 = {k:v for k,v in dict_1.items() if k == 'Uran'}
print(dict_1.values())

## counter() function allows to count elements
from collections import Counter
weaponry = ['gun', 'rifle', 'granade', 'knife', 'gun', 'granade']
wp_counter = Counter(weaponry)         ##  this command converts the list into a dictionary and counts elements
print(wp_counter)

## if you need to place your elements in DECREASING order you can use  most_common() function
wp_counter.most_common()
wp_counter.most_common(1)


print('Here we create a new dictionary')
weapon_2 = {'gun':2, 'rifle':1, 'granade':2, 'knife':1}
for i in weapon_2:
    print(weapon_2)

print('new code')

from collections import OrderedDict
weapon_3 = {'gun':2, 'rifle':1, 'granade':2, 'knife':1}
for item in weapon_3:
    print(weapon_3)


print('New line!')

def polin(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft != dq.pop():
            return False
    return True
polin('racecar')

print('New line')


