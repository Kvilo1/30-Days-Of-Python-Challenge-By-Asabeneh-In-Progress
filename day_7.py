#Exercises: level 1

# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")

it_companies.update("valve", "meta")

it_companies.remove("Facebook")

# if we wanted remove an item from set using remove() method, and it doesn't exist, it will raise an error. However, discard() method will not do such thing.

#Exercises: level 2

A.update(B)

A.intersection(B)

A.issubset(B)

A.isdisjoint(B)

omega = A.update(B) and B.update(A)

A.symmetric_difference(B)

del A 
del B

# Exercises: level 3

age_set = set(age)

print(len(age_set) < len(age)) # set is greater than list

"""
string is a string of words, intiger is an absolute number, tuple is a sorted and unchangeble list and a set is unsorted and changable list
"""

sentence = "I am a teacher and I love to inspire and teach people"

words = sentence.split()

uniqe_words = set(words)

print(len(uniqe_words))