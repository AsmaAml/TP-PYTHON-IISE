premier = input("Écrire une phrase :  \n")
deuxieme = input("Écrire une autre phrase :  \n")
troisieme = input("Écrire une troisième phrase :  \n")

phrase = [premier + "\n", deuxieme + "\n", troisieme + "\n"]

with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/phrases.txt", "w") as fichier:
    fichier.writelines(phrase)


