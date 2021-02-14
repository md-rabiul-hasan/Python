age = int(input("Enter your age : "))
if age < 0 :
    print("Negetive balance are not allowed")
elif age < 18 :
    print("You are under 18")
else:
    print("You are adult", end="")