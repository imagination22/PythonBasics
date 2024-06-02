thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon",'cake']
print(thislist)

thisNewList = ["apple", "banana", "cherry", "kiwi", "mango"]

a= [x for x in thisNewList]
print(a)

b = [x.upper() if x != 'apple' else 'pineapple' for x in thisNewList]
print(b)

c=[x.lower() if x == 'apple' else x.upper() for x in thisNewList ]
print(c)


d = [float(x) if x ==2 else x for x in range(10) if x<5]
print(d)

c.extend(b)
print(c)

list1 = [1,2,3,4]
list2= ['a','b','c']
list3 = list1 + list2
print(list3)
list4= ['x','y']
list2.extend(list4)
print(list2)
print(list3)
list3 = list1 + list2
print(list3)

print('extend demo')
print(list1)
print(list2)
print(list3)
print(list4)
list5 = ['m','n']
print(list5)
print('extend begin')
list1.extend(list5)
print(list1)
print(list2)
print(list3)
print('extend end')
lista = [5,6,7]
listb = lista
print(listb)
lista.extend(list1)
print(listb)

'''
listz = [float(x) if x != 7 else x for x in listb if listb.index(x) < len(listb) -2]
print(listz)

print(listz[-4:-1])

listz[2] = 7.0
print(listz)

listz[1:3] = [2.2,3.3,4.4]
print(listz)

'''