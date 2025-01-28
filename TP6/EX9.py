def get_positive_integer():
    while True:
        try:
            A = input("Veuillez saisir un entier positif : ")
            value = int(A)  
            if value <= 0:
                raise ValueError("L'entier doit être positif.") 
            return value  
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez essayer à nouveau.")

B = get_positive_integer()
print(f"Vous avez saisi l'entier positif : {B}")
