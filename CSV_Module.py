import csv
villains = [
['Doctor', 'No'],
['Rosa', 'Klebb'],
['Mister', 'Big'],
['Auric', 'Gpldfinger'],
['Ernst', 'Blofeld']
]
with open('Villains.txt', 'wt') as doc:
    csvout = csv.writer(doc)
    csvout.writerows(villains)

import csv
with open('Villains.txt', 'rt') as doc_2:
    csv.reader(doc_2)
    villains = [row for row in doc_2]
print(villains)

