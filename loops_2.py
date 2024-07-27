start_pt: int = int(input("please enter the starting point: "))
end_pt: int = int(input("please enter the ending point: "))
if start_pt < end_pt:
    for i in range(start_pt, end_pt + 1):
        print(i, end=' ')
else:
    print("The starting point has to be larger then the ending point!")