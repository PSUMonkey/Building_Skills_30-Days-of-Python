#Day 12: Modules
#10/11/2024

import modules #import the functions built in the modules.py module

def exercise_1():
    print(modules.random_user_id()) #call the random_user_id function from the modules module
    print(modules.user_id_gen_by_user()) #call the user_id_gen_by_user function from the modules module
    print(modules.rgb_color_gen()) #call the rgb_color_gen function from the modules module

def exercise_2():
    print(modules.list_of_hexa_colors(int(input("How many hexa colors do you want? "))))
    print(modules.list_of_rgb_colors(int(input("How many rgb colors sets do you want? "))))
    print(modules.generate_colors())

def exercise_3():
    #print(modules.shuffle_list(["value1","value2","value3","value4","value5","value6"]))
    print(modules.random_seven_array())

#exercise_1()
#exercise_2()
exercise_3()