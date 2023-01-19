
prenom = input("Donne ton prenom : ")
nom = input("Donne ton nom : ")

prenom2 = input("Donne un autre prenom : ")
nom2 = input("Donne un autre nom : ")

zebi = [str.capitalize(prenom), str.capitalize(prenom2)]
zebi2 = [str.upper(nom), str.upper(nom2)]

zebi.sort()
zebi2.sort()
print((zebi), (zebi2))
