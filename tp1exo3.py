print("Saisir nb de jours: ")
jours=int(input())


print("Saisir nb heures: ")
heures=int(input())


print("Saisir nb minutes: ")
minutes=int(input())


mois = (jours * 1440 + heures * 60 + minutes)
print("Il y a eu", mois, "minutes depuis le début du mois")
