print("ODD NUMBER ACCUMULATOR!!!")
print("Enter 10 numbers. We'll Sum only the odd ones")
total_sum = 0
for i in range (1, 11, 1):
    
    number = eval(input(f"Enter Number {i}: "))
    if number % 2 != 0:
        total_sum += number

    else:
        total_sum += 0
print("\nFrom 10 Inputted Numbers, The total Odd Amount is ", total_sum)
