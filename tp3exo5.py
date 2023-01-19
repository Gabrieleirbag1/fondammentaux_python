a = int(input("Donnez l'heure de début de la location : "))
b = int(input("Donnez l'heure de fin de la location : "))


if a < 0 or a > 24 and b < 24 or b > 24:
    print('Les heures doivent être comprises entre 0 et 24 !')

elif a == b:
    print("Attention ! l’heure de fin est identique à l’heure de début")

elif a > b:
    print("Attention ! le début de la location est après la fin ... ")

elif a >= 0 and b <= 7 or a >= 17 and b <= 24:
    res = b - a
    print(f"Vous avez loué votre vélo pendant\n{7-a} heure(s) au tarif horaire de 1.0 euro(s)\n0 heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")

elif a > 7 and b < 17:
    res = (b - a) * 2
    print(f"Vous avez loué votre vélo pendant\n0 heure(s) au tarif horaire de 1.0 euro(s)\n{b - a} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")

elif a >= 0 and b < 17:
    res = 7 - a + (b - 7) * 2
    print(f"Vous avez loué votre vélo pendant\n{7-a} heure(s) au tarif horaire de 1.0 euro(s)\n{b - 7} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")

elif a > 7 and b <= 24:
    res = (17 - a) * 2 + b - 17
    print(f"Vous avez loué votre vélo pendant\n{b - 17} heure(s) au tarif horaire de 1.0 euro(s)\n{17 - a} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")

elif a >= 0 and b <= 24:
    res = 7 - a + b - 17 + 20
    print(f"Vous avez loué votre vélo pendant\n{7-1+b-17} heure(s) au tarif horaire de 1.0 euro(s)\n{10} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")