 # fucntions with more than one inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# postional arguments
greet_with("Ganesh", "Nanded")

print(f"=" *28)

# keyword argumentts
greet_with(name="Ganesh", location="Nanded")

print(f"=" *28)

# or

greet_with(location="Nanded", name="Ganesh")
