import csv

# Données à écrire dans le fichier CSV
donnes = [
    ["Nom", "Age", "Ville"],
    ["ASMA", "22", "AGDIR"]
]


# Écrire les données dans le fichier
with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/contacts.csv", mode="w", newline="") as fichier:
    p = csv.writer(fichier)  
    p.writerows(donnes)  

