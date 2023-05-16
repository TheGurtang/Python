# we use json module to save massives of information into outter files for getting an excess to them later
import json

file_name = 'characters.txt'
file_1 = open('characters.txt', mode='w', encoding='Latin-1')           # here we create the outter file woth .txt extension


player_1 = {                            #  the first library with datas to be saved later
'player_name': 'Elric',
'experience': 'level 11',
'gold': 180,
'weapon': ['Stormbringer', 'dagger', 'scroll']
}

player_2 = {                             #  the second library with datas to be saved later
'player_name': 'Rachir',
'experience': 'level 12',
'gold': 90,
'weapon': ['Crimson_bow', 'curved_sword', 'black_arrows']
}

player_lib = []                        # here we create a list and append all our to-be-saved datas into it
player_lib.append(player_1)
player_lib.append(player_2)
print(player_lib)

json.dump(player_lib, file_1)          # here we use json.dump   for writing our selected data into preliminary-created file, which will be placed into the directory of  the current script-file
file_1.close()

# now it is also possible to read the saved file
with open('characters.txt', 'r')as file:
    read = file.read()
    print(read)
    read = file.close()

# now we also can write new data into the file


