# let create e-mail validation

import re    # here we import re-library

pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')    # here we insert a regular expression for e-mail validation
email = 'fgevara@yandex.ru'                                                    # here we introduce an e-mail for validation
test = pattern.search(email)                                                   # here we launch the code to match introduced e-mail with the regular expression
print(test)


# let create password validation

pattern_2 = re.compile(r'(^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? "]).*$)')   # here we insert a regular expression for password validation
password = '3_3a4-4A7.7a9!9A'                                                        # here we introduce our password for validation
test_2 = pattern_2.search(password)                                                  # here we launch the code to match the introduced password with the regular expression
print(test_2)


# suppose we want to create e-mail validator which picks the e-mail adress from the input-console
pattern_3 = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')       # here the regular expression for e-mail validation
email_2 = input('Please, insert your e-mail adress: ')                              # here we insert input-function for picking e-mail adress
test_3 = pattern_3.search(email_2)                                                  # here we launch the matching process
print(test_3)



def pas_check():
    pattern_4 = re.compile(r'(^.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*[!#$%&? "]).*$)')
    password_2 = input('Please, insert your password: ')
    if password_2 == True:
        print(pattern_4.search(password_2))
    else:
        print('You have provided the wrong password! Try once more! ')
print(pas_check())


