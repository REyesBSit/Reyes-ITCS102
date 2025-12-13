print("MULTIPLICATION TABLE MAKER!!!")

number = eval(input("Enter a Number: "))


print("\nMultiplication Table for ", number)
for i in range(1, 11, 1):

    multiply = i * number

    print(number, "X", i ,"=", multiply )
