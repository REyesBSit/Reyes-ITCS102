from getpass import getpass

print("Welcome to Bus A Incorporated")
name = getpass("Enter your name for data purposes: ")
fare = eval(input ("How much is your Fare Fee: "))
student = input("Are you currently a student (Yes or No): ").lower()

if student == 'yes':
	discount = fare * .2
	print("\nStudent Discount Amount: ", discount)
	print("Total Fare Fee: ", fare - discount)
	print("Thanks for choosing Bus A!!!")

elif student == 'no':
	print("\nRegular Total Fare Fee: ")
	print("Thanks for choosing Bus A!!!")

else:
	print("\nIncorrect Input!!! Please Try Again")
