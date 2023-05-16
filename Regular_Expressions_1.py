## suppose we have a string with many text where we have to find how many times certain elements occur

import re           ## we import regular expression library
list_1 = 'She mentioned this idea so many times that any other idea might have lost its idealogical meaning'


pattern = re.compile('idea')        ##  .compile('idea') sets a search for compliance in the text even if some letters are written differently
a = re.search('idea', list_1)       ## here we call re:search function and get this "<re.Match object; span=(19, 23), match='idea'>"
print(a.span())                     ##  it shows me where the looked for elemts occur as a tuples
print(a.start())                    ##  shows where element starts
print(a.end())                      ## shows where elements ends
print(a.group())                    ## it groups element and outputs it as atext


print('new test begin here!')
list_2 = 'So, on the next morning they embarked upon the way to the mountains without understanding in which way to head!'
b = re.search('way', list_2)
print(b.span())
                  ## so, let suppose I want to search ALL elements 'way' in the text
pattern = re.compile('way')
e = pattern.search(list_2)
c = pattern.findall(list_2)
print(c)

print('new test starts here!')
list_3 = 'WE have never thought about this book as a book provoking deep, analytical thoughts, literature like this is thought-provoking...'
a = re.search('book', list_3)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

pattern = re.compile('thought')
b = pattern.search(list_3)
b = pattern.findall(list_3)
print(b)

