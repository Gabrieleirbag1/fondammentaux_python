s=0
j=0
k=0
for i in range(10):
    a=int(input("Donnez une valeur : "))
    while a > 20 or a <0:
        a=int(input("Donnez une valeur : "))
    if a < 10:
        s+=1
    if a>=10 and a<15:
        j=j+1
    if a>=15:
        k+=1


print("Valeurs > 10 : ", s)
print ("Valeurs <= 10 et < 15 : ", j)
print ("Valeurs >= 15 : ",k)






