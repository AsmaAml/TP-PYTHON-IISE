# Cette fonction fusionne deux dictionnaires en combinant leurs clés et valeurs
def fusionner_dicts(dict1, dict2):
    # Crée une copie du dictionnaire dict1 pour éviter de modifier l'original
    dict = dict1
    # Parcours chaque clé et valeur du deuxième dictionnaire (dict2)
    for cle, valeur in dict2.items():
        # Si la clé existe déjà dans dict on additionne les valeurs
        if cle in dict:
            dict[cle] += valeur
        # Sinon on ajoute la clé et sa valeur dans dict
        else:
            dict[cle] = valeur
    # Retourne le dictionnaire fusionné
    return dict

dict1 = {"ASMA": 1, "HAJAR": 2}
dict2 = {"HAJAR": 1, "AMIRA": 2, "HAKIMA": 4}

# Affiche le résultat de la fusion des dictionnaires
print(fusionner_dicts(dict1, dict2))