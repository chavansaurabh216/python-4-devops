Day-1 | Introduction to Python and its Significance in DevOps

Python - founded in 1991 by Guido Van Rossum

Language Features -
	High level -- human readable
	versatile -- having the ability to do many different things or to adjust to new conditions (automation, devops, ml, ai, etc)
	dyanmically typed -- we dont have to specify the data types 

Key Features of Python - 
	1. Easy to learn and read
	2. Multi-purpose - versatile
	3. interpreted language - a programming language that executes instructions directly, line by line, without the need to compile the code into machine language first
	4. Rich Standard Lib
	5. Platform Independent
	6. Large Community and Ecosystem

Python in DevOps -
	1. Scripting and Automation
	2. Configuration Management
	3. CICD
	4. Monitoring and Logging

-------------------------------------------------------------------------------------------------------

Day-2 | Python syntax, data types, and variables

Data Types:
	Numeric Data Types
		1. Integer
		2. Float
		
	String
		1. ""
		2. ''
		3. '''<>'''
		
	Boolean
		1. true/false
		
	List
		Collection of multiple data types
		It is mutable ie. values can be change after declaration as well
		eg. a = [1, a, true, "yes"]
	
	Tuple
		Similar to List
		It is immutable ie. once declared values can not be changed
		eg. a = (1, a, true, "yes")
	
	Dictionaries
		Stored values in key value pair
		eg. my_dict = {'name': 'Saurabh', 'age': 24}
		print(my_dict['name])
		
	set
		Has all the unique values printed 
		eg. a = [1,1,2,2,2,3,3,3,4,5,6,6,6]
			print(a)  --> Output will be [1,2,3,4,5,6]
	
-------------------------------------------------------------------------------------------------------

DAY-3 | File handling in Python

	Working with Files
		Opening and Closing Files
		Reading from Files
		Writing to Files
		Appending to Files
	Working with Directories
		Creating Directories
		Listing Files and Directories
		Checking if a File or Directory Exists
		Deleting Files and Directories
		Recursive Directory Deletion

-------------------------------------------------------------------------------------------------------

Day-4 | User Inputs, Control Statements, Loops

Taking input from the user - by default string is taken as input

Statements
	If - else statement
	If - else ladder statement
	If - else nested statement
	break - stops the statement there when the given condition is satisfied
	continue - skips the iteration of the condition 

Loops
	for loop --> iterate through the given iterations
	while loop --> until the condition is statisfied loop will be executed
	List Comprehension --> List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
	Syntax - newlist = [expression for item in iterable if condition == True]	

-------------------------------------------------------------------------------------------------------

Day-5 | Functions & Modules

	Functions: A function is a block of organized, reusable code that performs a specific task
	Modules: A module is a file containing Python definitions and statements. Its like a template that will have the functions inside.

-------------------------------------------------------------------------------------------------------

Day-6 | Basic Networking Concepts
