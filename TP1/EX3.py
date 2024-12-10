# Cette fonction retourne l'intersection de deux ensembles donnés
def intersection_ensembles(ensemble1, ensemble2):
    # Utilisation de l'opérateur `&` pour calculer l'intersection des deux ensembles
    return ensemble1 & ensemble2


ensemble1 = {1, 2, 3}  # Premier ensemble
ensemble2 = {3, 4, 5}  # Second ensemble

# Appel de la fonction et affichage de l'intersection des deux ensembles
print(intersection_ensembles(ensemble1, ensemble2)) 