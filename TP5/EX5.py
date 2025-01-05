import json

etudiants = {
    "etudiant_1": {"nom": "Alice", "âge": 20, "note": 15.5},
    "etudiant_2": {"nom": "Bob", "âge": 22, "note": 18.0},
    "etudiant_3": {"nom": "Charlie", "âge": 21, "note": 14.0}
}


with open("C:/Users/user/OneDrive/Bureau/TP_Python_IISE/TP5/etudiants.json", mode="w") as fichier:
    json.dump(etudiants, fichier, ensure_ascii=False, indent=4)


