from getpass import getpass

username = 'Reyes'
password = 'ITCS102'

u = input("Enter Your Username: ")
p = getpass("Enter Your Password: ")

if username == u and password == p:
	print("Welcome to Python, ", username)

else:
	print("Access Denied, Please Try Again!!!")
