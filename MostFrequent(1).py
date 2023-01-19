L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

from collections import Counter
def most_frequent(lst):
    counter = Counter(lst)
    number, count = counter.most_common(1)[0]
    return number, count

number, count = most_frequent(L1)

print("Le nombre le plus fréquent dans la liste est le : ", number, "(",count, " fois)")



""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
