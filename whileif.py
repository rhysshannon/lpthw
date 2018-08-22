from random import randint
# the purpose of this is to test how to use while if with a sequence event action.
#protype a problem i had encountered in ex43.py where i could not make a cheat code work.  
code = (f"{randint(1,9)}{randint(1,9)}{randint(1,9)}")
# I tested guess with input using an int but this was problematic and more prone to errors leave as open and change the output if you have too...
guess = input("[keypad]> ")
guesses = 1

while guess != code and guesses <3:
    #nested if handles the behavour in the while statement. 
    # if is the cheat hack
    if guess == 'cheat':
        print(code)
    #else is normal behaviour
    else:
        print ("BZZZEDD!")
    guesses += 1
    guess = input("[keypad]> ")
if guess == code:
    print("awesome")

else:
    print("sheet")       

# conclusion this protyped a fix to make this work. 
