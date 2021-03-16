print('hello python\n')
a = 15
b = 20
print(a, b)
print(type(a))
print(id(a))
a, b = b, a
print(a, b)
#changed new id
print('a id is',id(a))
print('b id is ',id(b))
name=input('enter your name: ')
print("hello!! This is python code for hello {}".format(name))
