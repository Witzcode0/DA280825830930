# Python file handling involves interacting with files on your computer to perform operations such as creating, opening, reading, writing, and closing them. This functionality is crucial for data persistence and management in various applications.

# Key Concepts:
#     Opening Files: The open() function is used to open a file. It takes the file path and the mode as arguments.
#     file = open("filename.txt", "mode")

# Common modes include:
#     "r": Read (default)
#     "w": Write (creates a new file or overwrites an existing one)
#     "a": Append (adds content to the end of an existing file or creates a new one)
#     "x": Create (creates a new file and raises an error if it already exists) 
#     "r+": Read and write
#     "w+": Write and read
#     "a+": Append and read

# Reading Files: Once a file is opened in a read mode, you can use methods like:
#     read(): Reads the entire content of the file.
#     readline(): Reads a single line from the file.
#     readlines(): Reads all lines into a list of strings.

# Writing to Files: When a file is opened in a write or append mode, you can use:
#     write(string): Writes the specified string to the file.
#     writelines(list_of_strings): Writes a list of strings to the file. 
# Closing Files: It is essential to close files after use to release system resources and ensure data integrity.
#     file.close()

# Context Managers (with statement): The with open(...) as ...: statement is the recommended way to handle files as it automatically closes the file, even if errors occur.

# open or create a file
# file = open("example.txt", "w")

# file = open("sample.txt", "x")

# file = open("example.txt", "w")
# file = open("example.txt", "a")

# file.write("this is a python code.")

# file = open("sample.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# file = open("sample.txt", "w")
# lines =  ['this is a line no. 1\n', 'this is a line no. 22\n', 'this is a line no. 3\n', 'this is a line no. 4\n', 'this is a line no. 5\n', "this is a line no. 6\n"]

# file.writelines(lines)

# import os
# rename file
# os.rename("example.txt", "new_file.txt")

# remove file
# os.remove("new_file.txt")

# import uuid

# filename = f"{uuid.uuid4()}.py" 
# open(filename, "w")

# os.mkdir("test")
# os.chdir("test")
# os.mkdir("xyz")
# os.rmdir('xyz')

# os.system("py app.py")


# file = open("sample.txt", "r")
# print(file.read())
# file.close()
# print(file.read())

# with open("example.txt", "w") as file:
#     file.write("this is a python")





