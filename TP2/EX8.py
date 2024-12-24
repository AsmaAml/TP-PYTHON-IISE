# Définition de la classe Personne
class Personne:
    # Constructeur pour initialiser les attributs de la personne
    def __init__(self, nom, prenom, age):
        self.nom = nom  # Attribut pour le nom de la personne
        self.prenom = prenom  # Attribut pour le prénom de la personne
        self.age = age  # Attribut pour l'âge de la personne
        self.amis = []  # Liste vide pour stocker les amis de la personne

    # Méthode pour se présenter
    def se_presenter(self):
        return "Je m'appelle {} {}, j'ai {} ans et j'habite à Agadir.".format(self.nom, self.prenom, self.age)

    # Méthode pour ajouter un ami à la liste des amis
    def ajouter_ami(self, ami):
        self.amis.append(ami)  # Ajoute l'ami à la liste

    # Méthode pour afficher les amis de la personne
    def afficher_amis(self):
        if self.amis:  # Vérifie si la liste des amis n'est pas vide
            for am in self.amis:  # Parcourt et affiche chaque ami
                print(am)
        else:
            print("La liste des amis est vide.")  # Si la liste est vide, affiche un message

# Création d'une instance de la classe Personne avec nom "Asma", prénom "AMLAL", et âge 22
P = Personne("Asma", "AMLAL", 22)

# Affichage de la présentation de la personne
print(P.se_presenter())  # Affiche "Je m'appelle Asma AMLAL, j'ai 22 ans et j'habite à Agadir."

# Ajout d'un ami à la liste des amis
P.ajouter_ami("MIMI")

# Affichage des amis de la personne
P.afficher_amis()  # Affiche "MIMI"
