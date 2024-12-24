class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_info(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Salaire: {self.salaire} MAD"


class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes_supervises = []

    def ajouter_employe(self, employe):
        self.employes_supervises.append(employe)

    def afficher_employes_supervises(self):
        if not self.employes_supervises:
            print(f"{self.nom} n'a pas d'employés sous sa supervision.")
        else:
            print(f"Employés supervisés par {self.nom}:")
            for employe in self.employes_supervises:
                print(f"- {employe.afficher_info()}")


# Exemple d'utilisation
employe1 = Employe("Dupont", "Pierre", 3000)
employe2 = Employe("Durand", "Marie", 3500)

manager1 = Manager("Martin", "Luc", 5000)

# Ajouter des employés sous la supervision du manager
manager1.ajouter_employe(employe1)
manager1.ajouter_employe(employe2)

# Afficher les informations des employés supervisés
manager1.afficher_employes_supervises()

# Afficher les informations du manager
print(manager1.afficher_info())
