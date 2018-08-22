## Animal is a object (yes, sort of confusiing look at the extra credit)
class Animal(object):
    pass

## Class has a 
class Dog(Animal):

    def __init__(self,name):
        ## is a 
        self.name = name

## is a 
class Cat(Animal):

    def __init__(self, name):
        ## is a 
        self.name = name

## is a 
class Person(object):
    def __init__(self, name):

    ## is a 
        self.name = name

    ## person has a pet of some kind has a
        self.pet = None

## has a 
class Employee(Person):

    def __init__(self, name, salary):
    ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
    ## has a 
        self.salary = salary

    ## has a
class Fish(object):
    pass

class Salmon(Fish):
    pass

## has a 
class Haliburt(Fish):
    pass

## rover is a dog
rover = Dog("Rover")

##i is a 
satan = Cat("Satan")

## is a 
mary = Person("Mary")

## is a 
mary.pet = satan

# has a 
frank = Employee("Frank", 120000)

## is a 
frank.pet = rover

## has a
flipper = Fish()

## isa 
crouse = Salmon()
#has a 
harry = Haliburt()