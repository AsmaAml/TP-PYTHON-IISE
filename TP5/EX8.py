try:
    with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/inexistant.txt", "r") as fichier:
        contenu = fichier.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    print(f"Erreur : Le fichier 'inexistant.txt' n'existe pas.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")
