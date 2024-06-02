import port sys
print(sys.version)

a, b, c = (1, 2, 4)
print(a)
print(b)
print(c)

def myfunc():
    global a
    a = 2
    print(a)
myfunc()
print(a)


a = "hello\nworld"
b= "hello\rworld"
print(a)
print(b)
c= "hello \f world"
print(c)