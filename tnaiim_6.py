num1 = (input("Please enter a 4 digit number: "))
characters = [char for char in num1]
if 0 < len(num1) < 5:
    print(characters)
    print(f"The 2nd to last digit in your number is:  {num1[-2]}")

else:
    print("your number has too many digits.")