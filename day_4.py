"""

Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.


word_1 = "Thirty"
word_2 = "Days"
word_3 = "Of"
word_4 = "Python"
space = " "

print(word_1 + space + word_2 + space + word_3 + space + word_4)

Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print(word_1 + space + word_2 + space + word_3)
word_1 = "Coding"
word_2 = "For"
word_3 = "All"
space = " "

# Declare a variable named company and assign it to an initial value "Coding For All".

"""

word_1 = "Coding"
word_2 = "For"
word_3 = "All"
space = " "
company = word_1 + space + word_2 + space + word_3

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method

print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.

slice_obj = slice(6, 14)

print(company[slice_obj])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
