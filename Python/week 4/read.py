# Prompting user to enter file name
fileName = input("Enter file name : ")

# Create a new file with the file name given if it doesn't exist and write on it
file = open(fileName + ".pdf", "w")
file.write("i am learning how to code with python")

# Append a new content to the existing file
file = open(fileName + ".pdf", "a")
file.write(" from the ongoing PLP Africa scholaership program")


try:
    # Read the content of the file
    file = open(fileName + ".pdf", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    # Error to be display if file doesn't exist
    print("File not found. Please check the filename.")