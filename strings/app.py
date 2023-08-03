course = "Python's course for Beginners"
print(course)

email = """
Hi Gabriel,

Here is just a test run of our string email variable.

Thank you,
The hacking team

"""

print(email)

print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
print(course[0:3])
print(course[1:])
print(course[:6])
print(course[:])

# exercise
name = "Jennifer"
print(name[1:-1])

# working with formatted strings
first = "John"
last = "Smith"

# using concatenation to combine strings
message = first + " [" + last + "] is a coder"
print(message)

# using formatted output to combine strings
msg = f"{first} [{last}] is a coder"
print(msg)


# working with string methods
print(len(course))
print(len(email))
print(course.upper())
print(course)
print(course.lower())
print(course.find("o"))
print(course.replace("P", "J"))
print("python" in course)
print("Python" in course)

