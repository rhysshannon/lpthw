#this imports the modules we will use
from sys import argv
#this defines the variables we will be using
script, filename = argv
#variable that opens a file based on the filename variable entered earlier
txt = open(filename)
#this notifies the file and then opens the file. 
print(f"Here is your file {filename}:")
print(txt.read())
#asks for the file to be entered again. 
#closes the file
txt.close()
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()