highest_num = None
lowest_num = None

while True:
    num1 = int(input("Please enter a number: "))

    if num1 == -99:
        if highest_num is None and lowest_num is None:
            print("None")
        else:
            print(f"Highest number entered: {highest_num}")
            print(f"Lowest number entered: {lowest_num}")
        break

    if num1 > 0:
        if highest_num is None or num1 > highest_num:
            highest_num = num1
        if lowest_num is None or num1 < lowest_num:
            lowest_num = num1
    else:
        print("Please enter a positive number or -99 to exit.")
