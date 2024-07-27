num1: int = (input("Please enter a 4 digit number: "))
characters = [char for char in num1]
if 0 < len(num1) < 5:
    print(characters)
    print(f"The number that is on the most right index is: {num1[-1]}")

else:
    print("your number has too many digits.")