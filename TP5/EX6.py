import os

ancien_fichier = "C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/phrases.txt"
nouveau_fichier = "C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/anciennes_phrases.txt"

try:
    
    os.rename(ancien_fichier, nouveau_fichier)
    print(f"Fichier renommé : '{ancien_fichier}' -> '{nouveau_fichier}'")
    
    os.remove(nouveau_fichier)
    print(f"Fichier supprimé : '{nouveau_fichier}'")
except FileNotFoundError as e:
    print(f"Erreur : {e}")
except Exception as e:
    print(f"Erreur inattendue : {e}")
