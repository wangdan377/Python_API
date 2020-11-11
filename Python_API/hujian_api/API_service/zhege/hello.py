import sys
x = 45
#print(sys.modules)
# print(locals())
# print(globals())
# print(dir())

def aa(x):
    y = 5
    if x:
        z = x + y
    print(locals())
    print(globals())
    print(id(5))
    print(id(y))

aa(3)

print(id(aa))
print(aa)
print(id(x))
print(id(45))
