from sys import argv
#ok so standard argments
script, input_file = argv
# f becomes current file which is made up of the input file from argv
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, lets print the whole file in: \n")

print_all(current_file)

print("Now lets rewind, kind of like a tape")

rewind(current_file)

print("Lets print three lines:")
#sets the value of current_line at 1 then runs Print a line passing the line number and file its reading it off. 
current_line = 1
print_a_line(current_line, current_file)
#increments the line by one
current_line += current_line
print_a_line(current_line, current_file)
#increments the line but a further one. 
current_line += current_line
print_a_line(current_line, current_file)