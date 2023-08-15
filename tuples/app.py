#unlike arrays, tuples are immutable, meaning you can reassign tuples after creation
#creating a tuple
numbers = (1,2,3)

#printing all the items in a tuple
print(f"All the contents of the tuple are {numbers}")

#printing an item in a tuple
print(f"The content in position 0 is {numbers[0]}")

#checking the number of occurence of a content in a tuple
print(f"The number of itmes in this tuple is {numbers.count(2)}")

#checking for the index where an item resides
print(f"The value 2 is at index {numbers.index(2)}")

#aside from the magic methods, these are the only 2 methods that can be used in tuples

#unpacking
coordinate = (1,2,3)

#instead of having a long code like below
a = coordinate[0]
b = coordinate[1]
c = coordinate[2]

#you can use a feature called unpacking, it works with list as well 
x, y, z = coordinate

#this automatically assigns the contents of the tuple to the variables x, y and z respectively
print(x)
print(y)
print(z)

