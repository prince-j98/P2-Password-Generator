# user input: how long should the password be? (minimum 6)
# how many numbers in the password (the rest will be letters)
# generate password

import secrets
import random

print("Welcome to the Password Generator program!\nGenerate a 6-99 character password with little effort. \n")

try:
    pass_len = int(input("Please enter the length of your password (only enter number): "))
except ValueError:
    print("Invalid input. The password length can only be a number.")
    pass_len = 12
    print("Default password length (12) will be selected. \n")

try:
    num_in_pass = int(input("Please enter the number of alphabets you want in your password: "))
except ValueError:
    print("Invalid input. Your password will be equally divided into alphabets and numbers. \n")
    num_in_pass = int(pass_len/2)


if num_in_pass > pass_len:
    print("Invalid input. Numbers in your password cannot be more than the password length. \n")
    num_in_pass = int(pass_len/2)

if pass_len > 99:                                       # password should not be more than
    print("Password length is too large. Maximum password length has been selected.\n")
    num_in_pass = 99
elif pass_len < 6:
    print("Password length is too small. Minimum password length has been selected.\n")
    num_in_pass = 6

char_in_pass = pass_len - num_in_pass

print("\nYour password length is " + str(pass_len) + ", made of " + str(num_in_pass) + " letters and " + str(char_in_pass) + " alphabets. \n")

letters = "ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqurstuvwxyz"

password = ""

while len(password) < num_in_pass:
    password = password + str(secrets.randbelow(9))

while len(password) < pass_len:
    password = password + secrets.choice(letters)

pass_list = list(password)                              # to shuffle the password
random.shuffle(pass_list)
pass_gen = ''.join(pass_list)

print("Your password has been generated: \n" + str(pass_gen))               # final password