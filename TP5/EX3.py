
print("souhaite ajouter d'autres phrases à phrases.txt")
a = input("oui / non :  \n")
if a == "oui" :
    print("comme bien de phrases tu veux l'ajouter à phrases.txt")
    b = int(input("enter le nombre : "))
    i=0
    while i < b :
        phrase = input(f"Écrire une phrase {i+1}:  \n")
    
        with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/phrases.txt", "a") as fichier:
            fichier.write(phrase + "\n")
        i+=1

        