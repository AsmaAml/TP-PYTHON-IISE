# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"'{self.titre}' par {self.auteur} (Publié en {self.annee_publication})"

# Classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.livres = []  # Liste pour stocker les livres

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre}")

    def afficher_livres(self):
        if self.livres:
            print("Livres disponibles dans la bibliothèque :")
            for livre in self.livres:
                print(livre)
        else:
            print("La bibliothèque est vide.")

# Exemple d'utilisation
# Création de quelques livres
livre1 = Livre("1984", "George Orwell", 1949)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
livre3 = Livre("L'Étranger", "Albert Camus", 1942)

# Création d'une bibliothèque
bibliotheque = Bibliotheque()

# Ajout des livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Affichage des livres dans la bibliothèque
bibliotheque.afficher_livres()
