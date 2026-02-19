# loops

"""
1. Iterate 0 to 10 using for loop, do the same using while loop.

count_for = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for number in count_for: 
    print(number)

count_while = 0
while count_while <= 10:
    print(count_while)
    count_while += 1
"""

"""
2. Iterate 10 to 0 using for loop, do the same using while loop.

count_for = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0];

for number in count_for: 
    print(number)

count_while = 10
while count_while >= 0:
    print(count_while)
    count_while -= 1
"""

"""
3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######

hashy = "#"

for x in range(7):
    print(hashy)
    hashy += "#"
"""

"""
4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
    
"""

"""
5. Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

for x in range(11):
    print(x, " x ", x, " = ", x * x)
"""

"""
6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for items in lst: 
    print(items, end=" ")
"""

"""
7. Use for loop to iterate from 0 to 100 and print only even numbers

for x in range(101):
    if x % 2 == 0: 
        print(x)
"""

"""
Use for loop to iterate from 0 to 100 and print only odd numbers

for x in range(101):
    if x % 2 == 1: 
        print(x)

"""

"""
Exercises: Level 2
1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.

total = 0
for x in range(101):
    total += x

print(total)
    
"""

"""
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.

total_odds = 0
total_even = 0
for x in range(101):
    if x % 2 == 0:
        total_even += x
    if x % 2 == 1:
        total_odds += x

print(f"The sum of all evens is {total_even}. And the sum of all odds is {total_odds}")
"""

"""
1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# Will get back after taking "file handling" lesson #

"""

"""
2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = [fruits[i] for i in range(len(fruits) - 1, -1, -1)]
print("Reversed list:", reversed_fruits)
"""

"""
Go to the data folder and use the countries_data.py file.
I. What are the total number of languages in the data
II. Find the ten most spoken languages from the data
III. Find the 10 most populated countries in the world

# Will get back after taking "file handling" lesson #
"""