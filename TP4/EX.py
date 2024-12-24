class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        return f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}"


class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        return f"Puissance: {self.puissance} chevaux, Type de moteur: {self.type_moteur}"


class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)  # Appel explicite de la méthode de la classe Vehicule
        Moteur.__init__(self, puissance, type_moteur)  # Appel explicite de la méthode de la classe Moteur
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        vehicule_info = super().afficher_info()  # Utilisation de super() pour appeler la méthode de la classe parent
        moteur_info = super().afficher_moteur()  # Utilisation de super() pour appeler la méthode de la classe parent
        return f"{vehicule_info}, Nombre de places: {self.nombre_de_places}, {moteur_info}"


class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)  # Appel explicite de la méthode de la classe Vehicule
        Moteur.__init__(self, puissance, type_moteur)  # Appel explicite de la méthode de la classe Moteur
        self.type_moto = type_moto

    def afficher_info(self):
        vehicule_info = super().afficher_info()  # Utilisation de super() pour appeler la méthode de la classe parent
        moteur_info = super().afficher_moteur()  # Utilisation de super() pour appeler la méthode de la classe parent
        return f"{vehicule_info}, Type de moto: {self.type_moto}, {moteur_info}"


# Création d'une instance de Voiture
voiture1 = Voiture("BM", "X6", 2024, 150, "Essence", 5)

# Création d'une instance de Moto
moto1 = Moto("Tmax", "RX", 2023, 200, "Essence", "Sport")

# Affichage des informations
print(voiture1.afficher_info())
print(moto1.afficher_info())
