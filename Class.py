def how_many_years(start, rate, saving, target):
    balance = start
    years = 0

    while balance >= 0 and balance < target and years < 30:
        balance = balance *(1 + rate) + saving
        years += 1

    if balance >= target:
        return years
    else:
        return -1

x = how_many_years(1000, .1, 1000, 100000)
if x==-1:
    print("Unable")
else:
    print(x)