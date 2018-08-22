from sys import argv

script, filename = argv

print(f"Were going to erase {filename}.:")
print("If you dont want that. Hit CTRL-C (^C).")
print("If you do what that. hit RETURN")

input("?")
#set the variable target to the file. 
print("Opening the file...")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three line.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I am going to write these to the file.")
#uses the new line or line break to put the text on seperate lines
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("And finally, we close it")
target.close()