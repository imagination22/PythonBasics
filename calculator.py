a = int(input("enter 1st number : "))
b = int(input("enter 2nd number : "))

print("(a+b)/(a-b)*b%a**a")

c = (a-b)/(a+b)
print(c)

if (c < 0):
    print("negative number")
else:
    print("positive number")
print("default print, next elif")

if (c < 0 ):
    print("less than first number ")
elif(c == 0):
    print(" c is zero")
elif (c > 0):
    print("positive number")
print("default print , next for loop")


for i in range(0, 10, 2):
    print(i)
print("0 is first , 10 is last , 2 is difference")

count = 1

while( count < 10 ):
    count = count + 2
    print(count)