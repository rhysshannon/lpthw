from sys import argv

script, user_name = argv
prompt = 'XXX ' #should put the cursor in the input file

print(f"Hi {user_name}, Im the {script} script.")
print("Id like to ask you a few questions?")
print(f"do you like me  {user_name}?")
likes = input(prompt) #how you insert the prompt

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you have said {likes} about liking me. 
You live in {lives}. Not sure where that is. 
And you have a {computer} computer. Nice
""")
