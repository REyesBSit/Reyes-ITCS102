import random

print("Number Guessing Game!!!")
print("++++++++++++++++++++++++++++")

random_value = random.randint(1,5)
tries = 0

name = input("Input your name ---> ")

while True:
    num = eval(input("Guess the number from 1 to 5 ---> "))
    tries += 1
    
    if num == random_value:
        print("Winner!!!")
        break

    else:
        print("Incorrect Guess")
        continue

print(f"Hi {name}, Your Guess is Correct, Number of Tries = {tries}")