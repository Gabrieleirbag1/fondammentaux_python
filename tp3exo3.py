from random import *

i=randint(0,100)
g = 0
p = 0
print (i)
n = -1

while n != i:
    n = int(input())
    if n > i:
        print("Trop grand !")
        g += 1
    elif n < i:
        print("Trop petit !")
        p += 1
    elif n == i:
        print ("GG")

print ("Nombre de nombres trop grands :",g)
print ("Nombre de nombres trop petits :",p)
