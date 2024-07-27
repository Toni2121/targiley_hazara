num1 = (input("Please enter a 2 digit number: "))
characters = [char for char in num1]
if 0 < len(num1) < 3:
    print(characters)
    sum = int(num1[0]) + int(num1[1])
    print(f"your digit's sum is: {sum}")

else:
    print("your number has too many digits.")