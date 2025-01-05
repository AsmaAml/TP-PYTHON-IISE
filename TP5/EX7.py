import shutil
import os
with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/journal.txt", "w") as fichier:
        fichier.write("Jour 1 : Apprentissage Python.\n")
        fichier.write("Jour 2 : Exploration des modules.\n")
        fichier.write("Jour 3 : Création de scripts pratiques.\n")
    
source = "C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/journal.txt"  # Fichier à copier
destination = "C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/journal_copie.txt"  # Nom du fichier copié

try:
    shutil.copy(source, destination) # copie ce fichier dans un nouveau fichier nommé journal_copie.txt
    print(f"Fichier copié : '{source}' -> '{destination}'")
except FileNotFoundError:
    print(f"Erreur : Le fichier '{source}' n'existe pas.")
except Exception as e:
    print(f"Erreur : {e}")

A="C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/journal_copie.txt"
B="C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/archives"
os.makedirs(B) # cree un dossier 
shutil.move(A,B) # remplcer le fichier a un dossier



