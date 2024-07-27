minutes: int = int(input("please enter the length of the movie in minutes: "))
hours = minutes // 60
dakot = minutes % 60
if minutes > 60:
    print(f"the movie is {hours} hour(s) and {dakot} minute(s) long")