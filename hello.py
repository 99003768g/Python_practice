print('hello python\n')
a = 15
b = 20
print(a, b)
print(type(a))
print(id(a))
a, b = b, a
print(a, b)
#changed new id
print(id(a))