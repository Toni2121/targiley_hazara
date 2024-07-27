total: int = 0
while True:
    num1: int = int(input("please enter a number: "))
    if num1 == -99:
        print("None")
        break
    else:
        total += num1
        print(total)
        if num1 == -99:
            break