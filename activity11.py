temp = float(input("\nEnter temperature -->"))

if temp >= 1 and temp <= 20:
    print("\nIts Freezing Cold.")

elif temp >= 21 and temp <= 30:
    print("\nIts Shivering Cold")

elif temp >= 31 and temp <= 37:
    print("\nWhat a normal breeze")

elif temp >= 38 and temp <= 45:
    print("\nIts getting hot in there")\
    
elif temp >= 45  and temp <= 50:
    print("\nIts Very Hot!!!")

elif temp > 50:
    print("\nIts Dangerously Hot!!!!")

else:
    print("\nInvalid Input")