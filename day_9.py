# conditionals

"""
1. Get the user input("Enter your age: "). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.


age = int(input("Enter your age: "))

if age >= 18: 
    print("You are old enough to learn to drive.")
else: 
    missing_age = 18 - age
    print("You need", missing_age, "more years to learn to drive.")
"""

"""
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.


my_age = 23
your_age = int(input("enter your age: "))
age_gap = 23 - your_age

if age_gap == 1:
    print("you are 1 year younger than me")
elif age_gap == -1 : 
    print("you are 1 year older than me")
elif your_age < my_age:
    missing_age = 23 - your_age
    print("you are ", missing_age, "years younger than me")    
elif your_age > my_age:
    missing_age = your_age - 23
    print("you are ", missing_age, "years older than me")
else: 
    print("we are the same age!") 

"""

"""
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3


number_a = int(input("enter first number: "))
number_b = int(input("enter second number: "))

if number_a > number_b: 
    print(number_a, " is greater than", number_b)
elif number_a < number_b: 
    print(number_a, " is smaller than", number_b)
else:
    print("both numbers are equal")

"""

"""
Ecercises: Level 2

1. Write a code which gives grade to students according to theirs scores:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
score = int(input("write your score: "))

if score <= 59: 
    print("you got an F!")
if score >= 60 and score <= 69: 
    print("you got an D!")
if score >= 70 and score <= 79: 
    print("you got an C!")
if score >= 80 and score <= 89: 
    print("you got an B!")
if score >= 90 and score <= 100: 
    print("you got an A!")
"""

"""

Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

answer = input("write the month you are intrested with: ")

if answer == "September" or answer == "October" or answer == "November":
    print("it's Autumn")
elif answer == "December" or answer == "January" or answer == "February":
    print("it's Winter")
elif answer == "March" or answer == "April" or answer == "May":
    print("it's Spring")
elif answer == "June" or answer == "July" or answer == "August":
    print("it's Summer")
else: 
    print("the month you typed in is wrong, please try again")
"""
    
"""
3. The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

is_fruit_in = input("what fruit do you want to check? ")

fruits = ['banana', 'orange', 'mango', 'lemon']

if is_fruit_in in fruits: 
    print("That fruit already exist in the list")
else: 
    fruits.append(is_fruit_in)
    print(fruits)
"""

"""
Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
 
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person: 
    print(person["skills"][2])
else:
    None

if "Python" in person["skills"]: 
    print(person["skills"][4])
else:
    None

values = person["skills"]
JS, R, N, MDB, PY = values

if person["skills"] == JS and person["skills"] == R:
    print("He is a front-end developer")
elif person["skills"] == N and person["skills"] == MDB and person["skills"] == PY:
    print("he is a back-end developer")
elif person["skills"] == R and person["skills"] == N and person["skills"] == MDB:
    print("he is a front-end developer")
else:
    print("unknown title")   
    
if person['is_married'] == True and person['country'] == "Finland":
    print("Asabeneh Yetayeh lives in Finland. He is married.")
else:
    None

"""

