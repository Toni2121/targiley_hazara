max: int = int(input("please enter a number: "))
den: int = int(input("please enter another number: "))
for i in range(0, max + 1):
    if i % den == 0:
        print(i, end=' ')