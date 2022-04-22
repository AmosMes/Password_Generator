import random
import string
letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list("!@#$%^&*()")

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_digits = int(input(f"How many numbers would you like?\n"))

# Creating an empty list to be filled with the variables values in the for loops.
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_digits + 1):
    password_list.append(random.choice(digits))

# Randomly shuffle the list to not be predictable by hackers
random.shuffle(password_list)

# Creating an empty variable password to be a string output from the list password_list 
password = ""
for char in password_list:
    password += char

print(f"Your password is: \n {password}")
