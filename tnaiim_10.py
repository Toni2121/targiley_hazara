salary: float = float(input("please enter your salary: "))
if salary < 6000:
    print("there are no taxes applied!")
if 6000 <= salary <= 12000:
    taxes_applied = salary * 0.1
    print(f"There are tax applied, You need to pay: {taxes_applied}")
if 12000 < salary <= 18000:
    twenty_percent_taxes_applied = (salary - 12000) * 0.2
    ten_percent_taxes_applied = 12000 * 0.1
    total_taxes = twenty_percent_taxes_applied + ten_percent_taxes_applied
    print(f"There are tax applied, You need to pay: {total_taxes}")
if 18000 < salary <= 25000:
    thirty_percent_taxes_applied = (salary - 18000) * 0.3
    twenty_percent_taxes_applied = 18000 * 0.2
    ten_percent_taxes_applied = 12000 * 0.1
    total_taxes = twenty_percent_taxes_applied + ten_percent_taxes_applied + thirty_percent_taxes_applied
    print(f"There are tax applied, You need to pay: {total_taxes}")
if 25000 < salary <= 35000:
    forty_percent_taxes_applied = (salary - 25000) * 0.4
    thirty_percent_taxes_applied = 25000 * 0.3
    twenty_percent_taxes_applied = 18000 * 0.2
    ten_percent_taxes_applied = 12000 * 0.1
    total_taxes = twenty_percent_taxes_applied + ten_percent_taxes_applied + thirty_percent_taxes_applied + forty_percent_taxes_applied
    print(f"There are tax applied, You need to pay: {total_taxes}")
if 35000 < salary <= 50000:
    forty_five_percent_taxes_applied = (salary - 35000) * 0.45
    forty_percent_taxes_applied = 35000 * 0.4
    thirty_percent_taxes_applied = 25000 * 0.3
    twenty_percent_taxes_applied = 18000 * 0.2
    ten_percent_taxes_applied = 12000 * 0.1
    total_taxes = twenty_percent_taxes_applied + ten_percent_taxes_applied + thirty_percent_taxes_applied + forty_percent_taxes_applied + forty_five_percent_taxes_applied
    print(f"There are tax applied, You need to pay: {total_taxes}")
if salary > 50000:
    fifty_percent_taxes_applied = (salary - 50000) * 0.51
    forty_five_percent_taxes_applied = 50000 * 0.45
    forty_percent_taxes_applied = 35000 * 0.4
    thirty_percent_taxes_applied = 25000 * 0.3
    twenty_percent_taxes_applied = 18000 * 0.2
    ten_percent_taxes_applied = 12000 * 0.1
    total_taxes = twenty_percent_taxes_applied + ten_percent_taxes_applied + thirty_percent_taxes_applied + forty_percent_taxes_applied + forty_five_percent_taxes_applied +fifty_percent_taxes_applied
    print(f"There are tax applied, You need1 to pay: {total_taxes}")