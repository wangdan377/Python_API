import sys
print(sys.path)

a = [3,5,7,9]
*b,c = a
print(b)
print(c)

aa = {1:11,2:22}
x = aa.values()
print(x)

y = zip([1,2,3],['a','b','c'])
print(dict(y))