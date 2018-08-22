favourits = []

for i in range (0,10):
    name = input(" who is your top ten: > ")
    if 10-i == 1:
       print("list complete:")
    else:
        print(f'{9-i} choices remaining. Please add your next choice:')
    #append element
    favourits.append(name)


for i in favourits:
    print(f"Favourites were: {i}")

str(print(favourits))