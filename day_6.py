tpl = tuple()

sisters = ("magda", "asdas")
brothers = ("jasiu", "pierdzi", "stasiu")

siblings = sisters + brothers

print(len(siblings))

mother_and_father = ("anna","rafal")
family_members = mother_and_father + siblings

# Exercises: level 2

*sibling, mother, father = family_members

fruit = ("apple", "banana", "berry's")
vegetables = ("broccoli","carrot")
animal_products = ("cat food", "cat treats", )
food_stuff_tp = fruit + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

slicing = food_stuff_tp[3]
slicing_2 = food_stuff_tp[0:3]

print(slicing_2)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
is_here = "Estonia" in nordic_countries 
is_here_2 = "Iceland" in nordic_countries

print(is_here, is_here_2)
