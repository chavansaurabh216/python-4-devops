# An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits in the number

# Creating the function

def is_armstrong():

    number = int(input("Enter the number: "))

    if number < 0 :
        print("Enter the positive number")
    
    temp = number
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if number == sum:
        print("The number" , number , "is Armstrong number")
    else:
        print("The number" , number , "is not the Armstrong number")

# Calling the function

is_armstrong()