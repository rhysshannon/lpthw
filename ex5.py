my_name = 'Rhys Shannon'
my_age = 39 #this is my age
my_height = 78 #inches
my_heightft = my_height % 12
my_weight = 205 #pounds
my_weightkg = my_weight / 2.125
my_eyes = 'Green'
my_teeth = 'Whiteish'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"actually that is kind of borderline heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
print(f"my height {my_heightft} and weight {my_weightkg} in kg")

#this line is tricky. 
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and my {my_weight}, I get {total}).")