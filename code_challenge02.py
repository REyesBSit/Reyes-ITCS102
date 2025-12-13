amount = eval(input("Enter Amount to Deposit : "))
print("Heres the breakdown of amount you deposit: ")

thou = amount // 1000
amount = amount % 1000
print("1000 = ", thou)


fivehund = amount // 500
amount = amount % 500
print ("500 = ", fivehund)

twohund = amount // 200
amount = amount % 200
print ("200 = ", twohund)

hund = amount // 100
amount = amount % 100
print ("100 = ", hund)

fifty = amount // 50
amount = amount % 50
print ("50 = ", fifty)

twenty = amount // 20
amount = amount % 20
print ("20 = ", twenty)

ten = amount // 10
amount = amount % 10
print("10 = ", ten)

five = amount // 5
amount = amount % 5
print("5 = ", five)

one = amount // 1
print("1 = ", one)

