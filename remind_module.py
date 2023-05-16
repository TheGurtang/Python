vocab_1 = {
'a': 'currency',
'b': 'amount',
'c': 'Owner'
}

def operation_1():
    with open('writing_1.txt', 'w')as file_1:
        operate = file_1.write(str(vocab_1))
        print(operate)
operation_1()

def operation_2():
    with open('writing_1.txt', 'r')as file_2:
        operate = file_2.read()
operation_2()