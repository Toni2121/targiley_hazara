list1 = []

while len(list1) < 5:
    num1 = int(input("Please enter a number: "))
    list1.append(num1)
    print(list1)
    biggest_num = max(list1)
    biggest_number_index =list1.index(biggest_num)
    print(biggest_number_index + 1)