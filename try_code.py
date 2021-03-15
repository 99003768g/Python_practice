print("This is for try ")
try:
    a = 10
    b = 0
    c = a / b
    print(c)

except:
    print("Can't divide with zero")
finally:
    print("This block is printed no matter what")
