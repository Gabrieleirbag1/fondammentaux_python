L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
nbrdefois = []

mostval = 0
mostindice = 0
for i in range (len(L1)):
    nbr = 0
    for j in range (i, len(L1)):
        if L1[i] == L1[j]:
            nbr += 1
        if nbr>mostval :
            mostval = nbr
            mostindice = i

print(f'Il y a {mostval} fois le chiffre 7 dans la liste')

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
