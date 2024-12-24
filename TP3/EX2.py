class Personne:
    def __init__(self, nom, prenom, age):  # Correction de la méthode __init__
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_age(self):
        return self.__age

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_age(self, age):
        if age > 0:  # Vérification que l'âge est valide
            self.__age = age

    def afficher(self):
        return f"Nom: {self.__nom}, Prénom: {self.__prenom}, Âge: {self.__age}"


# Création d'une instance de la classe Personne
P1 = Personne("ASMA", "AMLAL", 22)  # Correction du constructeur

# Affichage des informations initiales
print(P1.afficher())

# Modification des attributs de l'objet
P1.set_age(45)
P1.set_nom("HAJAR")
P1.set_prenom("BOUMALK")

# Affichage des informations mises à jour
print(P1.afficher())
