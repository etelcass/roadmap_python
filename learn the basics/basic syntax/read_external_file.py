# I making 3 things. 
#   1. Creating a variable. 
#   2. Opening a file. 
#   3. Executing to read de file.
f = open("./../../textopruebados.py", "r")

# Printing the file content.
print(f.read())

# Printing a file in a fordward folder
f2 = open("./file/textoprueba.txt", "r")
print(f2.read())