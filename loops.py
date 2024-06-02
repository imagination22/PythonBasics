for x in range(6):
    print(x)
    if x == 3:
        print("breaking")
        break
    x += 1
else:
    print("finally finished !")

