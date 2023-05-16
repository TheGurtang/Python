derk = open('My_File.txt', 'wt')      ## here we create a txt-file by opening it
print('I have made it', file = derk)    ##  here we write the text into the file
derk.close()                            ## here we close the file

intod = 'Many years ago I contracted an intmacy with mister William Legrant who came from a noble Gogenot family which had lived on the island! After escaping from the chase he settled down in an old house on the desolated isle with his slave - Jupiter'
print(len(intod))
derk = open('My_File.txt', 'wt')            ## open the file
derk.write(intod)                            ##  inert the text from variable 'intod' into the file
derk.close()

##  reading the files with functions: read(), readline(), readlines()

reading_1 = open('My_File.txt', 'rt')   ## open the existing file
text = reading_1.read()                 ## create a new variable and launch read()-function
reading_1.close()
print(text)

##  reading the lines of hte file by means of readlines()-function

reading_2 = open('My_File.txt', 'rt')
lines = reading_2.readlines()           ##  this function reads lines of the text
reading_2.close()
for l in lines:
    print(l, end='')

## sometimes we prefer to operate file wothout typing close()-function all over again

with open('test_file_2.txt', mode='r+') as script:      ### forming our code like this we automatically close the file
    text = script.write('I had never een anything like that beofe. That is why I found this experiment so weird and set out so clumsily about that. Only my father knew how to operate that machine and it came up to me as a surprise that John had known how to operate it either. ')
    print(text)

## in case we need to add some text into hte file we have to use 'mode='a' which stands for 'append'

with open('test_file_2.txt', mode='a') as script_2:
    text = script_2.write('It was such a surprise to see him at our place!')        ## after mode='a' introduction in the code, we just add this piece of text
    print(text)


