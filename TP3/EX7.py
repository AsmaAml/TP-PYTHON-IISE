from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass


class Voiture(Vehicule):
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def deplacer(self):
        return f"La voiture {self.marque} {self.modele} roule sur la route."


class Bicyclette(Vehicule):
    def __init__(self, marque):
        self.marque = marque

    def deplacer(self):
        return f"La bicyclette {self.marque} se déplace à vélo."



voiture1 = Voiture("MERCEDES", "CE")
bicyclette1 = Bicyclette("Decathlon")

# Appel de la méthode 'deplacer' pour chaque objet
print(voiture1.deplacer())
print(bicyclette1.deplacer())
