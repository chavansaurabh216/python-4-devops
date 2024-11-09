# Opening a file in read mode
read_file = open('file_handling.md' , 'r')
read_content = read_file.read()
print(read_content)
read_file.close()

# Writing to Files
write_file = open('file_handling.md' , 'w')
write_file.write("This is written now")
write_file.close()

# Appending to Files
append_file = open('file_handling.md', 'a')
append_file.write("\nThis is appended")
append_file.close()

import os

# Creating Directories
os.mkdir("file_handling_test")
os.mkdir("file_handling_test_tree")

# Create a file
open('test.txt', 'a').close()
open('file_handling_test_tree/test.txt', 'a').close()

# Listing Files and Directories
os_list = os.listdir(".")
print(os_list)

# Checking if a File or Directory Exists
import os.path
dir_exist = os.path.exists("file_handling_test")        # Check if a directory exists
print(dir_exist)
file_exist = os.path.exists("readme.md")                # Check if a file exists
print(file_exist)

# Deleting Files and Directories
os.rmdir("file_handling_test")                          # Delete an empty directory
os.remove("test.txt")                                   # Delete a file

# Recursive Directory Deletion
import shutil
shutil.rmtree("file_handling_test_tree")