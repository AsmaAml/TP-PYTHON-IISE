with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/exemple.txt", "r") as fichier:
    lignes = fichier.readlines()
    for numero, ligne in enumerate(lignes, start=1):
        print(f"{numero} : {ligne.strip()}")
