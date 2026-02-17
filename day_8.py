cat = {}
cat["name"] = "fifunia"
cat["color"] = "white"
cat["breed"] = "neva masquarade"
cat["legs"] = 4
cat["age"] = "8 months"

student = {
    "first_name":"Bartek",
    "last_name":"Gorczyca",
    "gender":"Male",
    "age": 23,
    "marital status":"False",
    "skills":"programming",
    "country":"poland",
    "city":"wroclaw",
    "asddress":"dupa_jasiu"   
    }

print(len(student))

print(student.get("skills"))
print(type(student.get("skills")))

print(student)

keys = student.keys()
values = student.values()
print(keys, values)

student.items()