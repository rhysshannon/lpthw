#this one is like your scripts with argv
#you use def to tell python you want to make a script
#must have the : to work. 
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok that *args is pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")