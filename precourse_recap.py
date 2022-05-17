name = input("What is your name? ")
greeting = "Good morning"
goodbye = "See you later"

print(greeting + ', ' + name)

var1 = 13
var2 = 27

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

print(multiply(var1, var2))
print(subtract(var1, var2))

some_num = multiply(var1, var2) - subtract(var1, var2)
print(some_num)

my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

reversed_dictionary = {j: i for i, j in my_dictionary.items()}
print(reversed_dictionary)

for letter in my_dictionary:
    print(letter)

print(goodbye + ', ' + name)