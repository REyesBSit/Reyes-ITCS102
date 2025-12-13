from activity23_1 import *

print("WELCOME TO MY COMPILER PROGRAM")
name = input ("Hi, Visitor, what is your name? ---> ")

print(f"Hi {name}, select from the options below:")
print("A - Greet Name\nB - Greet with Name, Age, Location\nC - Triangle\nD - To Exit")

unli_loop = True

while unli_loop == True:
    choice = input("Select from A - D ---> ").lower()

    if choice == 'a':
        name = input("Please state your name ---> ")
        GreetWithName(name)
        continue

    elif choice == 'b':
        number = eval(input("Input any number ---> "))
        print(f"Factorial of {number} is {Factorial(number)}")
        continue

    elif choice == 'c':
        print("Creating Triangle, as requested....")
        code_challenge11()
        continue

    elif choice == 'd':
        print("Program Terminated")
        break

    else:
        print("Invalid Output...")
        break