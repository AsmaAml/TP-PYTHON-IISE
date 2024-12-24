# Classe Rectangle
class Rectangle:
    # Constructeur qui initialise la largeur et la hauteur du rectangle
    def __init__(self, largeur, hauteur):
        self.largeur = largeur  # Attribut pour la largeur
        self.hauteur = hauteur  # Attribut pour la hauteur

    # Méthode pour calculer la surface du rectangle
    def calculer_surface(self):
        return self.largeur * self.hauteur  # Surface = largeur * hauteur

    # Méthode pour calculer le périmètre du rectangle
    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)  # Périmètre = 2 * (largeur + hauteur)

# Création d'une instance de Rectangle avec largeur 5 et hauteur 3
R = Rectangle(5, 3)

# Affichage de la surface du rectangle
print(R.calculer_surface())  # Surface = 5 * 3 = 15

# Affichage du périmètre du rectangle
print(R.calculer_perimetre())  # Périmètre = 2 * (5 + 3) = 16
