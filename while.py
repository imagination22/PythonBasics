i = 0
while i < 5 :
    print(i)
    if i == 3 :
        print('breaking')
        break
    i += 1
else :
    print("completed")