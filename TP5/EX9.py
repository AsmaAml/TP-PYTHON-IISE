with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/fichier.txt", "r") as fichier :
    # Initialisation des compteurs
            total_lignes = 0
            total_mots = 0
            total_caracteres = 0

            # Parcourir chaque ligne du fichier
            for ligne in fichier:
                total_lignes += 1
                total_mots += len(ligne.split())  # Compter les mots par ligne
                total_caracteres += len(ligne)   # Compter les caractères par ligne

            # Les résultats
            print(f"Nombre total de lignes : {total_lignes}")
            print(f"Nombre total de mots : {total_mots}")
            print(f"Nombre total de caractères : {total_caracteres}")
