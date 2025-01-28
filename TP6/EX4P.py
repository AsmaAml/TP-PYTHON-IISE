class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"L'âge ne peut pas être négatif. Valeur fournie : {age}")
    print(f"L'âge est valide : {age}")


try:
    set_age(-5)  
except NegativeAgeError as e:
    print(f"Erreur : {e}")

try:
    set_age(25)  
except NegativeAgeError as e:
    print(f"Erreur : {e}")
