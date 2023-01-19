m = range(0, 10)
n = float(input("De quel table voulez-vous un nombre ? "))

for x in m:
    print(f"{n} * {x} = {round((n * x), 1)}")