# Cette fonction analyse un texte donné et retourne des statistiques sur le nombre de mots et de caractères

def analyse_texte(texte):
    # Divise le texte en mots en utilisant les espaces comme séparateurs
    # La méthode `split()` retourne une liste de mots
    mots = texte.split()

    # La méthode `replace(" ", "")` supprime tous les espaces avant de calculer la longueur avec `len()`
    nombre_caracteres = len(texte.replace(" ", ""))

    # Retourne un dictionnaire contenant le nombre de mots et de caractères sans espaces
    return {"nombre_mots": len(mots), "nombre_caracteres": nombre_caracteres}

# Demande à l'utilisateur d'entrer un texte
texte = input("Entrez un texte : ")

# Appelle la fonction 
print(analyse_texte(texte))
