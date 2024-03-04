# Function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to print a welcome message
def welcome_message(name):
    print("Welcome, " + name + "!")
    print("Have a great day!")

# Main function to demonstrate the use of other functions
def main():
    # Calculate the area of a rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_area(length, width)
    print("Area of the rectangle:", area)

    # Check if a number is even or odd
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(number, "is", result)

    # Print a welcome message
    name = input("Enter your name: ")
    welcome_message(name)

if __name__ == "__main__":
    main()
