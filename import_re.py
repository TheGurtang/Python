import re
source = 'Young Frankenstein'
m = re.findall('n', source)
print('Found', len(m), 'matches')


##  re.split() allows to split sequences by particular symbols and removing these symbols
import re
fr = 'I have never thought that we might lose so much money for one day'
i = re.split('h', fr)
print('Founded groups are: ', i)

print('New line')

## re.sub() allows to remove one elements from a sequence and remove it by another element
import re
seq = 'I have never thought that we might lose so much money for one day'
i = re.sub('have', 'had', seq)
print(i)

print('new line!')
