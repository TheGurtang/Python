
print('Task 1: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically')

def words_collect():
    a = input('Insert your words: ').split(' ')
    for i in a:
        if a.count(i) >1:      ## here we count 'i' in words collected from the input-console and check whether there are more than one word
            a.remove(i)        ## in case some words repet - such words are deleted
    a.sort()                   ##  .sort() function arranges everyting in alphabetical order
    print(' '.join(a))
print(words_collect())

print('Task 2: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line')
def num_picker():
    a = []
    for i in range(999, 3001):
        if i %2 ==0:
            a.append(i)
    return a
print(num_picker())


print('task 3: Write a program that accepts a sentence and calculate the number of letters and digits')
def lett_pic():
    b = []
    a = input('Insert your sentence: ').split(';')
    for i in a:
        b.append(i)
    for i in b:
        b.count(i)
print(lett_pic())
