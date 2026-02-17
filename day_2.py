#Day 2: 30 Days of python programming

#Exercises: Level 1
name = "Bartek"
last_name = "Gorczyca"
full_name = "Bartek Gorczyca"
country = "Poland"
city = "Wroclaw"
age = 23
year = 2003
is_married = False
is_true = True
is_light_on = True
pet_name, pet_age, pet_color = "Fifa", 1, "white"

#Exercises: Level 2

print(type(name), type(last_name), type(full_name), type(country), type(city), type(age), type(year), type(is_married), type(is_true), type(is_light_on))

print(len(name))
print("comparsion:", len(name), len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

radius = int(input("Enter radius: "))

help('keywords')
