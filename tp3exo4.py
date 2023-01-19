j=(input("Choisir while ou for : "))
m=0

while m==0:
  if j == "for":
    print("UTILISATION FOR")
    n = int(input('Entrez un nombre entier : '))
    f = 1
    for i in range(1, n+1):
      f = f * i
    print ("lA factorielle de ",n,"est",f)
    j = (input("Choisir while ou for ou stop: "))

  if j == "while":
    print("UTILISATION WHILE")
    N = int(input('Entrez un nombre entier : '))
    k = 1
    X = 1

    while k <= N:
        X = X * k
        k = k + 1

    print("le factorielle de l'entier ",N,"est",X)
    j = int(input("Choisir while ou for ou stop: "))

  if j == "stop":
    break

