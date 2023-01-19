print ("Entrez un nb entier :")
nb = int(input())

if nb > 0:
    print("Le nb est positif")
elif nb < 0:
    print("Le nb est négatif")

elif nb==0:
    print("le nb est 0 (et pair)")

if nb % 2 !=0:
    print("le nb est impair")

else:
    print("le nb est pair")