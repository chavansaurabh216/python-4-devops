# Takes user inputs for name and age.
# Uses an if-else statement to check if the user is eligible to vote based on their age.
# Prints numbers from 1 to 5 using a for loop.
# Calculates the factorial of a number using a while loop.

# Takes user inputs for name and age.
user_name = input("Enter the name: ")
user_age = int(input("Enter the age: "))

# Uses an if-else statement to check if the user is eligible to vote based on their age.
if user_age >= 18:
    print("Hi" , user_name , "Please vote for country")
else:
    print("Go to school beta")

# Prints numbers from 1 to 5 using a for loop.
for i in range(1,6):
    print(i)

# Calculates the factorial of a number using a while loop.
fact_num = int(input("Enter the number: "))
fact = 1
ref_num = 1

while ref_num <= fact_num:
    fact *= ref_num
    ref_num += 1

print("The factorial of", fact_num , "is", fact)