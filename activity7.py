bill = 0
bill = eval(input("Enter Your Initial Bill: "))

print("Here's your bil information over the past 6 months.\nDiscounts and Due Dates applied:\n")
print("1st Month: ", bill)

bill += 2500
print("2nd Month: ", bill)

bill *= .25
print("3rd Month: ", bill)

bill  /= .7355
print("4th Month: ", bill)

bill  -= 1292
print("5th Month: ", bill)

bill  *= -1852
print("6th Month: ", bill)

print("\nThanks for your patronage!!!")