x = 10
print(type(x))

y = x
print(f'the memory location of x is {id(x)}')
print(f'the memory location of y is {id(y)}')
if (id(x) == id(y)):
    print("x and y refer to same object")
print("===========================================")

x = x+1
print(f'the memory location of x is {id(x)}')
print(f'the memory location of y is {id(y)}')
if (id(x) == id(y)):
    print("x and y refer to same object")
else:
    print("x and y refer to same object")
print("===========================================")

z = 10
print(f'the memory location of z is {id(z)}')
if (id(x) == id(y)):
    print("y and z refer to same object")
else:
    print("y and z refer to same object")
print("===========================================")