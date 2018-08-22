from sys import argv
#not sure what this is 
from os.path import exists
#assign variables also if the to file does not exist, the program will create it. 
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")
#exists does a true false
print(f"Does the output file exist? {exists(to_file)}")
print("ready, hit the RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
#ok so we opened the outfile and then wrote the data to indata here. 
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
