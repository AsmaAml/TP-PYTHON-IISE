# Définition de la classe Chien
class Chien:
    # Constructeur de la classe
    def __init__(self, nom, race, age):
        self.nom = nom  # Attribut pour le nom du chien
        self.race = race  # Attribut pour la race du chien
        self.age = age  # Attribut pour l'âge du chien

    # Méthode pour simuler l'aboiement du chien
    def aboyer(self):
        print("Woof!")  # L'aboiement du chien

# Création d'une instance de la classe Chien
chien = Chien("JACK", "chien police", 5)  # Nom : JACK, Race : chien police, Âge : 5 ans

# Appel de la méthode aboyer pour faire aboyer le chien
chien.aboyer()


    