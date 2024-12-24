class Voiture:
    def __init__(self, marque, modèle, année):
        self.marque = marque
        self.modèle = modèle
        self.année = année

    def afficher_info(self):
        return "Marque: {}, Modele: {}, Année: {}".format(self.marque, self.modèle, self.année)

# Création des objets Voiture
V1 = Voiture("AUDI", "Q8", 2024)
print(V1.afficher_info())  # Affiche les informations de V1

V2 = Voiture("BMW", "X5", 2023)
print(V2.afficher_info())  # Affiche les informations de V2

V3 = Voiture("Mercedes", "GLA", 2022)
print(V3.afficher_info())  # Affiche les informations de V3
