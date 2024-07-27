num1: int = int(input("Please enter a number: "))
num2: int = int(input("Please enter another number: "))
result = 1
for _ in range(num2):
    result *= num1
print(f"The Hezkah of {num1} raised to the power of {num2} is: {result}")