# fruits = ["Apple", "Peach", "Pear"]
# for i in fruits:
#     print(i)
#
import random

# password generator program
password_letters = ['a', 'b', 'c', 'd']
password_numbers = ['1', '2', '3', '4']
password_special = ['@', '$', '(', ')']


no_of_letters = int(input("Enter the numbers of text u want in your password"))
no_of_numbers = int(input("Enter the number of numbers u want in your password"))
no_of_special = int(input("Enter the number of specia u want in your password"))


password = []
for char in range(0, no_of_letters+1):
    password.append( random.choice(password_letters))


for char in range(0, no_of_numbers+1):
    password.append(random.choice(password_numbers))

for char in range(0, no_of_special+1):
    password.append(random.choice(password_special))


print(password)
random.shuffle(password)
print(password)

passwords = ""
for char in password:
    passwords+=char
print(passwords)