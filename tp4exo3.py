nMax = 10
v1 = []
v2 = []

while True:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et " + str(nMax) + "] : "))
    if 1 <= n <= nMax:

        break
    print("\nLa taille saisie n'est pas valide, veuillez saisir une valeur comprise entre 1 et", nMax)

print("\nSaisie du premier vecteur 😊")
for i in range(n):
    v1.append(int(input("Entrez la composante v1[" + str(i) + "] : ")))

print("\nSaisie du second vecteur 😊")
for i in range(n):
    v2.append(int(input("Entrez la composante v2[" + str(i) + "] : ")))

# "append" rajoute les éléments à la fin de la liste

scal = 0
for i in range(n):
    scal += v1[i] * v2[i]

print("\nLe produit scalaire de v1 par v2 vaut :", scal)

