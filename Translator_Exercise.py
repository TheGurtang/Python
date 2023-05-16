## here we create an ordinary translator

with open('Translator_Exercise.txt', 'wt') as trans_1:
    text_1 = trans_1.write('Here I am now')
with open('Translator_Exercise.txt', 'rt') as trans_1:
    text =  trans_1.read()

from translate import Translator
tr = Translator(to_lang='zh')
trans_3 = tr.translate(text)
print(trans_3)

with open('Translator_Exercise.txt', 'wt') as trans_5:
    text_2 = trans_5.write(trans_3)



