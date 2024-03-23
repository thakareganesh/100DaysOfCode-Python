def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break # Break out of the loop if a factor is found
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} It is not a prime number")

    
num = int(input("Enter your number to check it is prime or not?\nEnter here: "))
prime_checker(number=num)
