num1: float = float(input("please enter a number: "))
num2: float = float(input("please enter another number: "))
result = num1 if num1 < num2 else num2
for _ in range(3):
    print(result)