num1 = (input("Please enter a 2 digit number: "))
characters = [char for char in num1]
if 0 < len(num1) < 3:
    print(characters)
    digit1 = int(num1[0])
    digit2 = int(num1[1])
    print(f"your reversed number is: {digit2}{digit1}")

else:
    print("your number has too many digits.")