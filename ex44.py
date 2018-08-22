# When you are doing this kind of specialization, there are three ways that the parent #and child classes
#can interact:
#INHERITANCE VERSUS COMPOSITION 215
#1. Actions on the child imply an action on the parent.
#2. Actions on the child override the action on the parent.
#3. Actions on the child alter the action on the parent. 
###
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")
    #override a class. 
    def overide(self):
        print("Parent Override")
    #altered
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
#will override the previous value. 
    def overide(self):
        print("CHILD override")
#will alter the value, this is useful when  you want to run a before and after activity over the same function. 
    def altered(self):
        #here the altered function is changed to child. in print
        print("CHILD, BEFORE PARENT altered()")
        #super calls parent value and alters it. 
        super(Child, self).altered()
        # PARENT ALTERED() IS PRINTED from the parent class. 
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

print(dad.implicit())
print(son.implicit())

print(dad.overide())
print(son.overide())

print(dad.altered())
print(son.altered())
