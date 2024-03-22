# We can concat the string and int (or any type of datatypes) together by multiple ways.

# this is my string
name = "Ganesha"

# this is my int
age = 23

# this is my float
height = 4.2


print("my name is " + name + " and I am " + str(age) + " years old and my height is " + str(height) + " inches")


print("My name is {} and I am {} years old and my height is {} inches".format(name, age,height))


print(f"My name is {name} and I am {age} years old and my height is {height} inches")