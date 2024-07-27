result = 0
num1: int = int(input("please enter a number: "))
num2: int = int(input("please enter another number: "))
for _ in range(num2):
    result += num1
print(f"The multiplication of {num1} and {num2} is: {result}")