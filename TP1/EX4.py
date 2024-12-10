# Cette fonction compte le nombre d'occurrences de chaque élément dans une liste donnée
def compte_occurences(liste):
    # Initialisation d'un dictionnaire pour stocker les occurrences
    occurrences = {}
    # Parcours de chaque élément dans la liste
    for mot in liste:
        # Si l'élément existe déjà dans le dictionnaire on incrémente son compteur
        if mot in occurrences:
            occurrences[mot] += 1
        # Sinon on l'ajoute au dictionnaire avec une occurrence initiale de 1
        else:
            occurrences[mot] = 1
    # Retourne le dictionnaire contenant les occurrences
    return occurrences

# Exemple d'utilisation avec une liste de mots
liste_mots = ["ASMA", "HAJAR", "ASMA", "HAKIMA", "HAKIMA", "ASMA"]
# Appel de la fonction et affichage du résultat.
print(compte_occurences(liste_mots)) 