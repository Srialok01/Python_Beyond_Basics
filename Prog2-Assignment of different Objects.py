z = 10
print(f'the memory location of z is {id(z)}')

"""
Any reference variable may later be assigned to object of different type 
eg - An object of Car can be asigned to x & hence it is called as dynamically typed language
"""


class Car():
    pass


z = Car()
print(f'the memory location of z is {id(z)}')
print(f'the type of z is {type(z)}')
