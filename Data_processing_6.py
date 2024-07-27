num1 = (input("Please enter a number: "))
digit1 = (input("Please enter a one digit number: "))
digits = [char for char in num1]
print(digits)
if digit1 in digits:
    print("True")
else:
    print("False")