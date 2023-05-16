## set_comprehension is particularly the same as with the list_comprehension, but using formed brakets {}


pick_it = [13,8,34,7,17]
picked_list_2 = [item for item in pick_it if item >= 10 ]           ##  here we execute list comprehension
print(picked_list_2)

take_it = {25,31,12,87,6}
take_it_2 = {item for item in take_it if item >= 15}           ## here we execute set comprehension
print(take_it_2)


dict_1 = {
    'a': 26,
    'b': 17
}
dict_2 = {v:i*2 for v,i in dict_1.items()}       ## here we execute dictionary_comprehension, having multiplied the values if each item by 2
print(dict_2)

dict_3 = {
    'a': 33,
    'b': 58
}
dict_4 = {k:v**2 for k,v in dict_3.items() if v%2!=0}    ##  here we executed dictionary_comprehension by chosing even and odd numbers
print(dict_4)

def my_selection(list):
    sel_list = []
    for item in list:
        sel_list.append( (item + item) * 3)
    return sel_list
print(my_selection([35]))

my_selection_1= [23,45,76,123,45,181]
my_selection_3 = ['Karlos', 'Will', 'Jam']
my_selection_2 = [item for item in my_selection_1 if item >= 75]
print(my_selection_2)
print(list(zip(my_selection_2, my_selection_3)))

class list_selector():
    def __init__(self, odd_analisis, even_analisis, zip_analisis):
        self.odd_analisis = odd_analisis
        self.even_analisis = even_analisis
        self.zip_analisis = zip_analisis
    def odd_analisis_fun(self):
        siph_1 = [123,766,234,195,231,348,187,573]
        siph_2 = [item for item in siph_1 if item %2 !=0]
        print(siph_2)
    def even_analisis_fun(self):
        siph_4 = [123, 766, 234, 195, 231, 348, 187, 573]
        siph_5 = [item for item in siph_4 if item % 2 == 0]
        print(siph_5)
    def zip_analisis_fun(self):
        print('The first operations result: ', odd_analisis_fun)
        print('The seconds operations result: ', even_analisis_fun)

list_selector_1 = list_selector('Looking for odd ones', 'Looking for even ones', 'Zipping two sets of data together')
print('The first operation: ', list_selector_1.odd_analisis)
list_selector_1.odd_analisis_fun()
print('The second operation: ', list_selector_1.even_analisis)
list_selector_1.even_analisis_fun()
print('The third operation: ', list_selector_1.zip_analisis)
list_selector_1.zip_analisis_fun()