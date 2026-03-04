# Modules
import random
import string

"""
1. Write a function which generates a six digit/character random_user_id.

def random_user_id():
    characters = string.ascii_letters + string.digits 
    randomiser = "".join(random.choices(characters, k = 6))
    return randomiser

print(random_user_id())
"""

"""
2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn't take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    characters_num = int(input("Enter the number of characters: "))
    ID_num = int(input("how many id's would you like to generate?: "))
    characters = string.ascii_letters + string.digits
    
    for randomiser in range(ID_num - 1):
        randomiser = "".join(random.choices(characters, k = characters_num))
        print(randomiser)
    return randomiser 

print(user_id_gen_by_user())
"""

"""
3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    first_digit = random.randrange(0, 255)
    second_digit = random.randrange(0, 255)
    third_digit = random.randrange(0, 255)
    return f"rgb({first_digit},{second_digit},{third_digit})"

print(rgb_color_gen())
"""

"""
Exercises: Level 2 
1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


def list_of_hexa_colors(num):
    characters = string.hexdigits 
    colors = []
    for _ in range(num):
        hex = ''.join(random.choices(characters, k = 6))
        colors.append(f"#{hex}")
    return colors
print(list_of_hexa_colors(3))

"""

"""
2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def rgb_color_gen(num):
    colors = []
    for _ in range(num):
        first_digit = random.randrange(0, 255)
        second_digit = random.randrange(0, 255)
        third_digit = random.randrange(0, 255)
        colors.append(f"rgb({first_digit}, {second_digit}, {third_digit})")
    return colors 

print(rgb_color_gen(3))

"""

"""
3. Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(type, num):
    if type == "hexa":
        characters = string.hexdigits 
        colors_hexa = []
        for _ in range(num):
            hex = ''.join(random.choices(characters, k = 6))
            colors_hexa.append(f"#{hex}")
        return colors_hexa
    elif type == "rgb":
        colors_rgb = []
        for _ in range(num):
            first_digit = random.randrange(0, 255)
            second_digit = random.randrange(0, 255)
            third_digit = random.randrange(0, 255)
            colors_rgb.append(f"rgb({first_digit}, {second_digit}, {third_digit})")
        return colors_rgb         
print(generate_colors("rgb", 3))
"""

