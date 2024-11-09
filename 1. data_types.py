# Numeric Types
num_int = 20
num_float = 22.22
print(num_int , num_float)

# String
name = "Saurabh"
print(name)

# Boolean --> true or false data stored
is_salaried = True
print(is_salaried)

# List  --> stores multiple datatypes but are mutable in nature
my_hobbies = ["Cricket", "Movies", True , 2]
print(my_hobbies)
print(my_hobbies[2])
my_hobbies[2] = False
print(my_hobbies)

# Tuple --> stores multiple datatypes but are immutable in nature
my_negative = (1,2,3,"nothing")
print(my_negative)
print(my_negative[1])
# my_negative[1] = 1    // Tuple are immutable in nature
# print(my_negative)

# Dictionary  --> data stored in key value form
personal = {"Name": "Saurabh", "Last":"Chavan","Age": 25}
print(personal)
print(personal["Age"])
personal["City"] = "Banglore"
print(personal)

# Set --> prints unique values
something = {1,1,1,2,2,2,4,3,4,5,5,3,4,5,6,1,2,3,4}
print(something)