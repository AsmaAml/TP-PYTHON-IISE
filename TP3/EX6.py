class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher_info(self):
        return f"{self.nom} - {self.prix} MAD"


class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit  # Une instance de la classe Produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.prix * self.quantite


class Panier:
    def __init__(self):
        self.commandes = []  # Liste de commandes

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total_panier(self):
        total = 0
        for commande in self.commandes:
            total += commande.calculer_total()
        return total



# Exemple d'utilisation
produit1 = Produit("Ordinateur", 15000)
produit2 = Produit("Clavier", 300)

# Création de commandes
commande1 = Commande(produit1, 2)  # 2 ordinateurs
commande2 = Commande(produit2, 3)  # 3 claviers

# Création du panier
panier = Panier()

# Ajout des commandes au panier
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

# Affichage du total du panier
print(f"Total du panier: {panier.calculer_total_panier()} MAD")
