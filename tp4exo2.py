nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
somme = 0.0

notes = []

for x in range(nombreEtudiants):
    somme=(float(input(f'Note etudiant {x} : ')))
    notes.append(somme)
    moyenne += somme

moyenne = moyenne / nombreEtudiants
print("Moyenne de classe",moyenne)


for i in range(nombreEtudiants):
    print(f'{i}|{notes[i]}|{moyenne-notes[i]}')
