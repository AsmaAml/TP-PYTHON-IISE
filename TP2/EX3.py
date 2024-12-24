class CompteBancaire :
    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(self.solde)
        else:
            print("Le montant doit être supérieur à 0")
    def retirer(self,montant): 
        if montant>0 :
            if self.solde>montant :
                self.solde -= montant  
                print(self.solde)
            else :
                print("le solde nest pas suffisant")
        else:
            print("Le montant doit être supérieur à 0")

    def afficher_solde(self):
        return "Tutilaire: {},Solde: {}".format(self.titulaire,self.solde)
    
B1=CompteBancaire("Hajar",1000)
print(B1.afficher_solde())  # Affiche les détails du compte

B1.deposer(500)  # Ajoute 50 au solde
print(B1.afficher_solde())  # Affiche le nouveau solde

B1.retirer(300)  # Retire 30 du solde
print(B1.afficher_solde())  # Affiche le nouveau solde

B1.retirer(1500)  # Essaie de retirer plus que le solde