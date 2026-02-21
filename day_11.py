# Functions

"""
1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(x,y):
    return x + y

print(add_two_numbers(x = 5, y = 2))
"""

"""
2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    return 3,14 * r * r

print(area_of_circle(r = 3))
"""

"""
3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if nums == type(int):
            return ("type is not int. Type int argument instead")
        else:
            total +=num
    return total

print(add_all_nums(1, 2, 3, 4))
"""

"""
4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(C):
    return (C * 9 / 5) + 32 

print(convert_celsius_to_fahrenheit(20))
"""

"""
5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month == "September" or month == "October" or month == "November":
        return "it's Autumn"
    elif month == "December" or month == "January" or month == "February":
        return "it's Winter"
    elif month == "March" or month == "April" or month == "May":
        return "it's Spring"
    elif month == "June" or month == "July" or month == "August":
        return "it's Summer"
    else:
        return "that's not a month, type again"

print(check_season("December"))
"""

"""
6. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    
    return (y2 - y1)/(x2 - x1)
"""

"""
7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c): 
    delta = b**2 - 4 * a * c
    root = delta**0.5
    if root == 0:
        x0 = -b/2 * a 
        return x0
    elif root > 0: 
        x1 = (-b - root)/ 2 * a
        x2 = (-b + root)/ 2 * a
        return ("x1 = ", x1,"x2 = ", x2)
    elif root < 0: 
        return("no roots")
    
print(solve_quadratic_eqn(a = 2,b = 4,c = 5))
"""

"""
9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
    return [lst[items] for items in range(len(lst) -1, -1, -1)]
                                       
print(reverse_list([1, 2, 3, 4, 5, 6]))
"""

"""
10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
     
    item = [items.capitalize() for items in lst]
    return item

print(capitalize_list_items(["apple", "banana","berry"]))
"""

"""
11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(item, lst):
    lst.append(item)
    return lst

print(add_item(item = "apple", lst = ["banana", "kiwi"]))

"""
"""
12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(item, lst):
    lst.remove(item)
    return lst

print(remove_item(item = "apple", lst = ["apple", "kiwi", "banana"]))
"""

"""
13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(nums):
    total = 0
    for x in range(1, nums + 1):
        total += x
    return total
print(sum_of_numbers(50))
"""

"""
14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(nums): 
    total = 0
    for x in range(1, nums + 1):
        if x % 2 != 0:
            total += x
    return total

print(sum_of_odds(7))
"""

"""
15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(nums):
    total = 0
    for x in range(1, nums + 1):
        if x % 2 == 0:
            total += x
    return total
print(sum_of_even(6))
"""

"""
Exercise: Level 2

1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
"""

def even_and_odds(nums):
    for x in range(nums):
        if x % 2 == 0:
            x += x
    return x 

print(even_and_odds(100))