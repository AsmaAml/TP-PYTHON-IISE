class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        return "Je m'appelle {} {}, j'ai {} ans et j'habite à Agadir.".format(self.nom, self.prenom, self.age)

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)  # Appel correct au constructeur parent
        self.matricule = matricule

    def etudier(self):
        return "Je suis étudiant avec le matricule {}.".format(self.matricule)

# Exemple d'utilisation
P = Personne("Asma", "AMLAL", 22)
print(P.se_presenter())

E = Etudiant("Asma", "AMLAL", 22, "D134734876")
print(E.se_presenter())
print(E.etudier())
