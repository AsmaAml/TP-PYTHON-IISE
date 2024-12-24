class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    # Propriété pour le nom
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
            self.__nom = nom

    # Propriété pour le prix
    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if prix > 0:
            self.__prix = prix
        else:
            self.__prix = 0  # Valeur par défaut si le prix est incorrect

    # Méthode pour calculer le prix avec remise
    def calculer_prix_remise(self, remise, seuil):
        if self.prix > seuil:
            return self.prix * (1 - remise / 100)
        return self.prix

    # Méthode pour afficher les informations du produit
    def afficher(self):
        return f"Produit: {self.nom}, Prix: {self.prix} MAD"


# Exemple d'utilisation
produit1 = Produit("Ordinateur", 15000)
produit2 = Produit("Clavier", -300)  # Prix invalide, sera remplacé par 0

print(produit1.afficher())  
print(f"Prix avec remise: {produit1.calculer_prix_remise(10, 5000)} MAD")  

print(produit2.afficher())  
print(f"Prix avec remise: {produit2.calculer_prix_remise(10, 5000)} MAD") 
