import math
from abc import ABC, abstractmethod

# Classe abstraite Forme
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

# Classe Rectangle
class Rectangle(Forme):
    def __init__(self, L, l):
        self.L = L
        self.l = l

    def calculer_surface(self):
        return self.L * self.l

# Classe Cercle
class Cercle(Forme):
    def __init__(self, R):
        self.R = R

    def calculer_surface(self):
        return math.pi * (self.R ** 2)

# Création d'objets et calcul des surfaces
R1 = Rectangle(10, 5)  
print(f"Surface du rectangle : {R1.calculer_surface()}")

C1 = Cercle(7) 
print(f"Surface du cercle : {C1.calculer_surface()}")
