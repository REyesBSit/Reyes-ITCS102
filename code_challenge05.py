howmany = eval(input("Enter How Many Output: "))

factorial = 1

for i in range(howmany, 0, -1):
    factorial *= i

print("The Factorial of ", howmany, "is ", factorial)
