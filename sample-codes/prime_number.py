# Printing the prime number in the range

start = 2
end = 10

print("The prime numbers between" , start , "to" , end , "are:")

for num in range(start, end+1):
    if num > 1 :
        for i in range (2, num):
            if (num % i) == 0:
                break
            else:
                print(num)