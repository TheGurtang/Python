my_list_1 = []

for mean in 'Greetings':     ##  this is our usual way for making up a list
    my_list_1.append(mean)
print(my_list_1)


my_list_2 = [mean for mean in 'Greetings']    ##  here we get the same result by creating a loop in one line
print(my_list_2)


my_list_3 = []
for nums in range(0, 100):
    my_list_3.append(nums)
print(my_list_3)
                            ## or in the one line

my_list_4 = [nums for nums in range(0, 100)]      ## here we get the same result in one line
print(my_list_4)

my_list_5 = [nums*2 for nums in range(0,100)]    ## here we print not simply a list in range from 0 to 99, but also multiplied each number on 2
print(my_list_5)

my_list_6 = [nums**2 for nums in range(0,100)]    ## here we made nums in square
print(my_list_6)

my_list_7 = [nums**2 for nums in range(0,100) if nums %2 ==0]    ## we extend the code by inserting if - CONDITION which cheks even-numbers only
print(my_list_7)