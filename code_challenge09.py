import time

i = eval(input("How Many Seconds Before Lift Off?: "))
print("\tCountdown Starts at...")
print(i)
for countdown in range (i, 0, -1):
    time.sleep(1)
    i -= 1
    print(i)
print("Lift Off!!!")
