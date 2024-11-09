# Taking the input from the user
# By default string the type of data taken so we are changing it to required
print("################## Taking Input from user ##################")
user_input = int(input("Enter something: "))
print(user_input)
print(type(user_input))


# Simple if-else statements
print("################## Simple if-else statements ##################")
age = int(input("Enter the age: "))

if age>=18:
    print("Bhai bada ho gaya re tu")
else:
    print("Ghungru babu baccha hai apna")

# Ladder of if-else statement
print("################## Ladder of if-else statement ##################")
score = int(input("Enter the score: "))

if score >= 91:
    print('A')
elif score >= 81:
    print('B')
elif score >= 71:
    print('C')
elif score >= 61:
    print('D')
else:
    print('Bhai padh lee')

# Nested if-else statement
print("################## Nested if-else statement ##################")
age_prashant = int(input("Enter the age of Prashant: "))
age_saurabh = int(input("Enter the age of Saurabh: "))

if age_prashant > age_saurabh:
    print("Enter the if statement")
    if age_prashant > 25:
        print("Age of Prashant is more than 25")
    elif age_prashant < 25:
        print("Age of Prashant is less than 25")
    else:
        print("Age of Prashant is", age_prashant)
elif age_prashant < age_saurabh:
    print("Enter the elif statement")
    if age_saurabh > 25:
        print("Age of Saurabh is more than 25")
    elif age_prashant < 25:
        print("Age of Saurabh is less than 25")
    else:
        print("Age of Saurabh is", age_saurabh)
else:
    print("Else statement is executed")


# break statement
print("################## break statement ##################")
break_var = 5

for i in range(10):
    if i == break_var:
        break
    print(i)

# continue statement
print("################## continue statement ##################")
continue_var = 5

for i in range(10):
    if i == continue_var:
        continue
    print(i)

# For Loop
print("################## For Loop ##################")
for i in range(5):
    print(i)

for_list = [1,2,3,4,5]
print("For Loop for iterating a list")
for i in for_list:
    print(i)

# While Loop
print("################## While Loop ##################")
count = 0
while count < 10:
    print(count)
    count += 1

# Looping through Dictionaries
print("################## Looping through Dictionaries ##################")
dict_loop = {"Name":"John" , 'Age': 25 , "Hobby": "Nothing"}

# Print all key names in the dictionary, one by one
print("################## Print all key names in the dictionary, one by one ##################")

for key in dict_loop:
    print(key)

print("OR by using keys() method")

for key in dict_loop.keys():
    print(key)

# Print all values in the dictionary, one by one
print("################## Print all values in the dictionary, one by one ##################")
for values in dict_loop:
    print(dict_loop[values])

print("OR by using values() method")

for values in dict_loop.values():
    print(values)

# Loop through both keys and values, by using the items() method
print("################## Loop through both keys and values, by using the items() method ##################")

for key , values in dict_loop.items():
    print(key , values)

# Loop Control with Else
print("Loop Control with Else")
print("You can use an else block with a loop, which executes when the loop completes without hitting a break")

for i in range(5):
    print(i)
else:
    print("Loop completed without break")

# Break to interupt the loop
for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Loop completed with break")
print("Loop completed with break")

# Continue statement to skip the iteration in the loop
for i in range(5):
    if i==3:
        continue
    print(i)
else:
    print("Loop completed with continue statement")

# List Comprehension

print("Creating a list based on the existing list")

fruits_list = ["apple" , "grapes" , "mango" , "cherry"]
print(fruits_list)
new_fruits_list = []

for x in fruits_list:
    if "a" in x:
        new_fruits_list.append(x)
print("Printing the items from fruit list which consists of 'a':" , new_fruits_list)

# Now using the List Comprehension we can write the code in one line

new_fruits_list_list_comp = [x for x in fruits_list if "a" in x]

print("Print the List using the List Comprehension:" , new_fruits_list_list_comp)