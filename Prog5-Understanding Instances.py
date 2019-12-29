"""
Variables defined in class are available to the instances
"""
print("====================Instance=====================")
class MyClass(object):
    var = 10

this_obj = MyClass()
that_obj = MyClass()

print(this_obj.var)
print(that_obj.var)

print("====================Instance Methods===============")
print()
"""
Accessing methods from instances
"""
class salutation():
    def hello(self):
        print("Hello there !!")
        print(self)

obj = salutation()
print(obj)
obj.hello()
print()
print("====================Instance Attributes===============")
"""
Instance attributes 
"""
print()
import random
class Mynewclass():
    def dothis(self):
        self.randaom_no = random.randint(1,10)

myinst = Mynewclass()
print(myinst.dothis())
print(myinst.randaom_no)


