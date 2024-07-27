list1: list[int] = []
last_input: int = 0
highest_temp: int = 0
lowest_temp: int = 0
for i in range(1, 13):
    while True:
        try:
            month_degree: int = int(input(f"please enter the temperature of month number {i}: "))
            if -5 <= month_degree <= 40:
                if last_input == 0 and month_degree == 0:
                    continue
                list1.append(month_degree)
                last_input = list1[-1]
                avg = sum(list1) / len(list1)
                highest_temp = max(list1)
                lowest_temp = min(list1)
                print("correct data")
                break
            else:
                print("wrong data, please enter a temperature between -5 and 40")
        except Exception as e:
            print(f"invalid input ---{e}--- please try again")

print(list1)
print(f"The average temperature throughout the year was: {avg}")
print(f"The highest temperature throughout the year was: {highest_temp}")
print(f"The lowest temperature throughout the year was: {lowest_temp}")
