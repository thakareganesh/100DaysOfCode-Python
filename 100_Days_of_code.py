# Day 5
"""
#loop example 1
fruits = ["Apple", "Mango","Banana" , "Guava","Dragonfruit"]
for fruit in fruits:
    #print(fruit)
    print(fruit + " Pie")
print(fruits)
"""
# for loop in range(): Adding even numbers upto specific number
"""
target = int(input("Enter your number: "))
even_sum = 0
for number in range(2, target + 1, 2):
    # accumulate even_sum here
    #print(number)
    even_sum += number
print(f'the sum of the even number upto {target} is: {even_sum}')
"""
#another method
target = int(input("Enter your number: "))
alternative_num = 0
for number in range(1,target+1):
    if number % 2 == 0:
        alternative_num += number
print(f"the sum of the even number upto {target} is: {alternative_num}")
