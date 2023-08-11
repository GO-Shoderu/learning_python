is_hot = False
is_cold = False

if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

#exercise 
price = 1000000

print("Price of a house is R" + str(price))
user_credit = input("Enter credit status (g/b): ")
user_income = input("Enter income: ")

is_high = False

if (int(user_income) > (0.2 * price)):
    is_high = True

print("Using the and operator will result in")
if user_credit.lower() == "g" and is_high:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print("Using the or operator will result in")
if user_credit.lower() == "g" or is_high:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print("Using the and not operator will result in")
if user_credit.lower() == "g" and not is_high:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

