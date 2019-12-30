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
        print("Hello there !!")  # Hello there !!
        print(self)  # <__main__.salutation object at 0x000001E7194B97C8>


obj = salutation()
print(obj)  # <__main__.salutation object at 0x000001E7194B97C8>
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
        self.random_no = random.randint(1, 10)


myinst = Mynewclass()
# print(myinst.dothis()) # This will print None as the function doesn't have return type
myinst.dothis() # Random no generation is done at the time of calling do this method
print(myinst.random_no)
"""
myinst.random_no : this syntax is generally used to access a class variable, But there is no class variable here
 as random value (i.e instance value) is set inside of an instance itself and hence its invoked by instance itself
"""
