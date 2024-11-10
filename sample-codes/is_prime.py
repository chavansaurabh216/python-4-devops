# This is the code to check if the number is prime or not

number = int(input("Enter the number: "))
is_prime = True

for i in range (2 , number):
    if number % i == 0:
        is_prime = False
        break

if is_prime :
    print("The" , number , "is prime number")
else:
    print("The", number , "is not a prime number")