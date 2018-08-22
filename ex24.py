print("lets pracice everything")
print("Uou\d need to know \' about escapes with \\ that do")
print("'\n newlines and \t tabs")

poem = """
\tthe lovely world
with logic so firmly planted
cannont discern \n the needs of love 
nor comprehend passion from intuition
and requires and explanation
\n\t\t where there is none. 
"""


print("------------")
print(poem)
print("-------------")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to form a string
print("with a starting point of: {}".format(start_point))
#its just like wiht an f'' string
print(f"Wed have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("wed have {} beans, {}, jars, and {} crates.".format(*formula))

