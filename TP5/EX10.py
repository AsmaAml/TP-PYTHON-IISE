import csv
import os

# Nom du fichier CSV
FICHIER_CSV = "C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/Contact_fichier.csv"

# Vérifier si le fichier existe déjà, sinon créer avec les en-têtes
def initialiser_fichier_csv():
    if not os.path.exists(FICHIER_CSV):
        with open(FICHIER_CSV, mode="w", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["Nom", "Téléphone", "Email"])

# Ajouter un contact au fichier CSV
def ajouter_contact():
    nom = input("Entrez le nom : ")
    telephone = input("Entrez le téléphone : ")
    email = input("Entrez l'email : ")

    with open(FICHIER_CSV, mode="a", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, telephone, email])
    print(f"Contact ajouté : {nom}, {telephone}, {email}")


# Afficher tous les contacts
def afficher_contacts():
    with open(FICHIER_CSV, mode="r") as fichier:
        reader = csv.reader(fichier)
        next(reader)  # Ignorer l'en-tête
        print("\nTous les contacts :")
        for ligne in reader:
            # Vérification que la ligne contient des données suffisantes
            if len(ligne) >= 3:
                print(f"Nom: {ligne[0]}, Téléphone: {ligne[1]}, Email: {ligne[2]}")
            else:
                print("Ligne mal formatée ou vide ignorée.")


# Rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Entrez le nom à rechercher : ")
    with open(FICHIER_CSV, mode="r") as fichier:
        reader = csv.reader(fichier)
        next(reader)  # Ignorer l'en-tête
        for ligne in reader:
            if ligne[0].lower() == nom_recherche.lower():
                print(f"Contact trouvé : Nom: {ligne[0]}, Téléphone: {ligne[1]}, Email: {ligne[2]}")
                return
        print(f"Le contact '{nom_recherche}' n'a pas été trouvé.")

# Supprimer un contact
def supprimer_contact():
    nom_suppression = input("Entrez le nom du contact à supprimer : ")
    contacts = []

    with open(FICHIER_CSV, mode="r") as fichier:
        reader = csv.reader(fichier)
        header = next(reader)  # Lire l'en-tête
        contacts.append(header)  # Ajouter l'en-tête aux contacts
        for ligne in reader:
            if ligne[0].lower() != nom_suppression.lower():
                contacts.append(ligne)

    with open(FICHIER_CSV, mode="w", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerows(contacts)
    print(f"Contact '{nom_suppression}' supprimé.")

# Menu principal
def menu():
    initialiser_fichier_csv()
    while True:
        print("\n=== Menu ===")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("by")
            break
        else:
            print("Option non valide, veuillez réessayer.")

if __name__ == "__main__":
    menu()
