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
with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/contacts.csv", mode="r", newline="") as fichier:
    p=csv.reader(fichier)
    for i,ligne in enumerate(p) :
        if i==0 :
            continue
        print(f"Nom : {ligne[0]}, Age : {ligne[1]}, Ville : {ligne[2]}")


