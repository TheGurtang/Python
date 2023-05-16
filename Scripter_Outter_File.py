script_1 = open('test_file_3.txt', 'wt')
text = script_1.write('WE should be sure that the function works well! ')
script_1.close()
print(script_1)
script_1 = open('test_file_3.txt', 'rt')
text = script_1.read()
print(text)
script_1.close()

script_1 = open('test_file_3', mode='a')
text = script_1.write('Seems like it is working!')
print(text)
script_1.close

with open('test_file_3', 'rt') as script_1:
    text = script_1.read()
    print(text)