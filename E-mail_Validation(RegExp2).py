#  Here we try to create an e-mail validation algorytm

import re                # at this step we import  'regular expression' library

pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')          #  we took the expression from the outter web-site with already-made solution
string = 'dexter@yandex.ru'                                                      # here we introduce an e-mail adress for validation
a = pattern.search(string)                                                         # here we call the function of SEARCHING through the given adress
print(a)

# Assume we want to create a password checker

