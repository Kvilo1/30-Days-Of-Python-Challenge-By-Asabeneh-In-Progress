lst = list()

list_2 = ["item_1", "item_2", "item_3", "item_4", "item_5"]

print(len(list_2))

print(list_2[0], list_2[2], list_2[3])

mixed_data_types = ["Bartek", 23, 185, False, "dupa"]

it_companies = ["facebook","google","microsoft","apple","ibm","oracle","amazon"]

print(it_companies)

print(len(it_companies))

# print(it_companies[0], it_companies[3], it_companies[7])

it_companies[0] = "valve"

# 11

it_companies.append("chuj")

# 12

it_companies.insert(5, "masdm")

strings = ["#; "]
it_companies.extend(strings)
print(it_companies)

does_exist = "valve" in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

all_it_companies = it_companies[0:2]
all_it_companies = it_companies[5:7]
all_it_companies = it_companies[5]

del it_companies[0]

del it_companies[5]

del it_companies[7]

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
all_lists = it_companies + front_end + back_end

full_stack = all_lists.copy()

#exercises: level 2 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print(ages.max(), ages.min())