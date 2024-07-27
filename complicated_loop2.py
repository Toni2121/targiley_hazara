total_for: int = 0
total_against: int = 0
total_abstain: int = 0
list1 = []
veto_spot = -1

first_for_index = None
first_against_index = None

for i in range(1, 45):
    while True:
        try:
            vote: int = int(input("what is your vote (for - 1) (against - 2) (abstain - 3) (veto - 4):"))
            if vote == 1:
                total_for += 1
                list1.append(total_for)
                print(f"For - {total_for}")
                print(list1)
                if first_for_index is None:
                    first_for_index = i
                break
            elif vote == 2:
                total_against += 1
                list1.append(total_against)
                print(f"Against - {total_against}")
                print(list1)
                if first_against_index is None:
                    first_against_index = i
                break
            elif vote == 3:
                total_abstain += 1
                list1.append(total_abstain)
                print(f"Abstain - {total_abstain}")
                print(list1)
                break
            elif vote == 4:
                veto_spot = i
                print(f"Veto by country number: {veto_spot}")
                break
            else:
                continue
        except Exception as e:
            print(f"Invalid input ---{e}--- please try again")

    if vote == 4:
        break

print(f"Final results: For - {total_for}, Against - {total_against}, Abstain - {total_abstain}")
print(f"First country to vote for: {first_for_index}")
print(f"First country to vote against: {first_against_index}")
print(list1)
