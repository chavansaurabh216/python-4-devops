# Printing the prime number in the range

# Creating a function

def prime_range():
    start_num = int(input("Enter the start number: "))
    end_num = int(input("Enter the end number: "))

    print("The Prime numbers between the range" , start_num , "and" , end_num , "are: ")

    for num in range (start_num , end_num + 1 ):
        if num > 1:
            for i in range (2 , num):
                if (num % i) == 0:
                    break
            else:
                print(num)

# Calling the function

prime_range()