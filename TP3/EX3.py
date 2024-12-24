import math

# Classe Rectangle
class Rectangle:
    def __init__(self, L, l):
        self.L = L
        self.l = l

    def calculer_surface(self):
        return self.L * self.l

# Classe Cercle
class Cercle:
    def __init__(self, R):
        self.R = R

    def calculer_surface(self):
        return math.pi * (self.R ** 2)

# Fonction pour afficher les surfaces
def afficher_surface(formes):
    for forme in formes:
        print(f"Surface: {forme.calculer_surface()}")

# Exemple d'utilisation
formes = [
    Rectangle(10, 5),  
    Cercle(7),         
    Rectangle(3, 4)    
]

afficher_surface(formes)
