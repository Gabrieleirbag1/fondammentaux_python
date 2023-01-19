BASE = int(4)
fromage = float(800.0)
eau = float(2)
ail = int(2)
pain = float(400)


print("Combien de convives ?")
nbConvives = int(input())

fq = (fromage * nbConvives) / BASE
eq = (eau * nbConvives) / BASE
aq = (eau * nbConvives) / BASE
pq = (pain * nbConvives) / BASE



print("-Il faut", fq, "g de fromage pour", nbConvives, "personnes.")
print("-Il faut", eq, "L d'eau pour", nbConvives, "personnes.")
print("-Il faut", aq, "ails pour", nbConvives, "personnes.")
print("-Il faut", pq, "g de pain pour", nbConvives, "personnes.")
