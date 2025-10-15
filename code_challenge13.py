name = input("Enter Name ---> ")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\nODD NUMBER SELECTOR, press 0 to stop the loop")
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
number = 0
output = ""
while True:
    x = eval(input("\nEnter a random number ---> "))
    
    if x % 2 == 1:
        print("ODD NUMBER IS DETECTED...")
        number += x
        output += str(x) + " "
        continue

    elif x == 0:
        print("Ending the loop...")
        break

    else:
        print("EVEN NUMBER IS DETECTED...")
        continue

print(f"Hi {name}, the sum of all ODD numbers is {number}")
print(f"ODD numbers include the ff ---> {output}")