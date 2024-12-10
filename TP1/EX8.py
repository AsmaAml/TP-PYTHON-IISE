# Cette fonction calcule la somme d'un nombre variable d'arguments
# je utilise l'opérateur *args pour accepter un nombre illimité de valeurs en entrée
def somme_varargs(*args):
    # Utilisation de la fonction intégrée `sum` pour additionner tous les arguments
    return sum(args)

print(somme_varargs(1, 2, 3, 4)) 