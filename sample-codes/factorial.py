# Python Program to Find the Factorial of a Number

# Taking the input from the user
fact_num = int(input("Enter the number: "))

# Creating the function
def factorial():
    # Define the initial value of factorial as 1
    fact = 1

    # Use for loop to iterate till the input number
    for i in range(1 , fact_num + 1):
        # While iterating we are incrementing the value by multiplying it with the value of i
        fact *= i
    
    # Printing the final output
    print (f"The Factorial of {fact_num} is {fact}")

# Calling the function
factorial()