def read_file(filename):
    try:
        file = open(filename, "r")  # Ouvrir le fichier en mode lecture
        content = file.read()  # Lire le contenu du fichier
        return content
    except FileNotFoundError:
        raise FileExistsError()
    finally:
        file.close()  # Fermer le fichier si ouvert
        

# Chemin du fichier
fichier = r"C:\Users\user\OneDrive\Bureau\TP_Python_IISE\TP6\exemple.txt"

# Lecture du fichier
try:
    contenu = read_file(fichier)
    if contenu:
        print(f"Contenu du fichier '{fichier}':\n{contenu}")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
