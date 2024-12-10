# Cette fonction calcule la factorielle d'un nombre entier donné de manière récursive
def factorielle(n):
    # Cas de base : la factorielle de 0 est définie comme étant 1
    if n == 0:
        return 1
    else:
        # Appel récursif : n * factorielle(n-1)
        return n * factorielle(n - 1)
print(factorielle(3))  
