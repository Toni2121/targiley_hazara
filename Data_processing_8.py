num1 = int(input("Please enter a number: "))
is_rishoni = True
for i in range(2, num1):
    if num1 % i == 0:
        is_rishoni = False
        break
if num1 <= 1:
    print(f"The number {num1} is not a number rishoni.")
elif is_rishoni:
    print(f"The number {num1} is a number rishoni.")
else:
    print(f"The number {num1} is not a number rishoni.")