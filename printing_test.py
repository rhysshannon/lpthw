days = "Mon Tues Wed"
hdays = "here are the days:  "
print("here are the days: ", days) # prints days after the text no matter what it is. 

# could also use the following variant

print(f'here are the days:  {days}')

#another way of doing the same thing

print_format = "{}{}" # if you put a space inbetween the {} it will add a space duh
print_format_nl = "{}\n\t{}" #same with new line and tab included


print(print_format.format(hdays, days))
print(print_format_nl.format(hdays, days))

dSplit = days.split(" ")

for d in dSplit:
    print(d)

fat_cat = """
This is a list:
\t* item 1 
\t* item 2
\t* item 3
\t* item 4
\t* item 5
\t* item 6
\t* item 7
thats it""" 

print(fat_cat) 
print("how old are you?", end="\n")
nex = input()
print(f'you are {nex} years old!')