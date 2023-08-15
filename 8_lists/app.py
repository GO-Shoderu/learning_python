#list
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

#printing the entire list
print(names)

#printing just a content wihtin a list using an index
print(names[0])
print(names[2])

#prints the last item in the list
print(names[-1])
print(names[-2])

#printing a range of item from the second position to the end
print(names[2:])

#printing a range of item from the second to 4 position
print(names[2:4])

#modifying the item in a list
names[0] = 'Jon'

#exercise for finding the largest number in a list
numbers = [10,15,0,3,28,9,85,26,14,99,10]
largest = 0

print(f"The contents of the list are {numbers}")

for number in numbers:
    if number > largest:
        largest = number
        print(f"The largest value for now is {largest}")

print(f"Largest number in the list is {largest}")

#working with 2 dimensional list
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

#printing the item in the list
print(matrix[0][1])

#making alteration to the content of the list
matrix[0][1] = 20
print(matrix[0][1])

#printing all the items in the list
print(f"The contents of the list are {matrix}")

#attempting to iterate through the 2Dlist without using the resources

for row in matrix:
    for col in row:
        print(col)

#tada!!! I got it right ... 

#working with list methods

#adding items to a list
numbers.append(160)

#inserting items
#array_name.insert(position, item)
numbers.insert(0,100)

#removing all the items in a list
#numbers.clear()

#removing the last item in a list
numbers.pop()

#finding the existence of an item
print(f"100 is in position {numbers.index(100)}")

#you can also make use of "in"
print(100 in numbers)

#you can use in before using the index function because if 50 isn't present
#in the list of items it will break the code and stop it from running 

#there are other functions like 
#count - for counting the occurence of an item (numbers.count(5))
#sort - for arranging the list of items in ascending order (numbers.sort())
#reverse - for arranging the list of items in descending order (numbers.reverse())
#copy - for copying the content of a list to another variable (numbers2 = numbers.copy())

