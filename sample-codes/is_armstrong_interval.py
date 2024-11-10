# Python Program to Find Armstrong Number in an Interval

start_range = int(input("Enter the start number: "))
end_range = int(input("Enter the end number: "))

def is_armstrong_interval():

    for num in range(start_range , end_range + 1):
        # order of number or number of digits
        number_digit = len(str(num))

        # Initialize the sum
        sum = 0

        # Making temp variable as num
        temp = num

        # Running while loop to fing the armstrong numbers
        while temp > 0 :
            # taking one by one  digit out
            digit = temp % 10
            
            # Adding the sum of power to number of digit
            sum += digit ** number_digit

            # Making the digit an integer value if it is float
            temp //= 10
        
        # Printing the final result
        if num == sum :
            print(num)

print("The armstrong numbers between", start_range , "and" , end_range , "are: ")
is_armstrong_interval()