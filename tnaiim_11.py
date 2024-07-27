height: float = float(input("How tall are you in cm? "))
age: int = int(input("How old are you? "))
if 8 < age < 18 and height > 115:
    print("You're allowed to enter!")
elif age > 18 and height > 100:
    print("You're allowed to enter!")
else:
    print("you are not allowed to eneter!")