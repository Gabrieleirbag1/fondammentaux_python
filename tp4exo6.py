m31 = [1,3,5,7,8,10,12]
date = input("entrez une date sous la forme jjmmaaaa:")
22022022
jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])

if mois == 2:
    if ((annee%4==0 and annee%100!=0) or annee%400):
        if jour > 29