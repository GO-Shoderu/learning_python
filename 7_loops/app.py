#creating and working with a while loop
i = 1

while i <= 5:
    print("*" * i)
    i+=1

print("Done while looping")

guess_count = 0
guess_limit = 3
secret_number = 9

while guess_count < 3:

    guessed_value = int(input("Guess the secret number: "))

    if guessed_value == secret_number:
        print("You made the right guess, you won!!!")
        break
    else:
        print("The guessed value is wrong, try again!!!")

    guess_count+=1

else:
    print("Unfortunately you didn't get any guesses right!!!")


#creating and working with a for loop
#various ways of working with a for loop
for item in "Python":
    print(item)

for item in ["Gabs", "Chris", "Nubby"]:
    print(item)

for item in [1,2,3,4,5,6,7,8,9,10]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

#using 2 steps
for item in range(5, 10,2):
    print(item)

#little exercise
prices = [10, 20, 30]
total = 0

for item in prices:
    total += item

print("Total price is " + str(total))

#having nested loops 
print("list of coordinates needed for navigation")
for x in range(4):
    for y in range(3):
        print(f"coordinates: ({x}, {y})")
