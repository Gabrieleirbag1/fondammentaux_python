m = int(input())
k = 1
x = 1

if m == 0:
    print("1")

while k <= m:
    x = x * k
    k = k + 1

print("la factorielle de ", m, "est", x)