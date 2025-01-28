def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("La division par zéro n'est pas autorisée.")
    return a / b
try:
    result = safe_division(10, 0)
    print(f"Résultat : {result}")
except ZeroDivisionError as e:
    print(f"Erreur : {e}")

try:
    result = safe_division(10, 2)
    print(f"Résultat : {result}")
except ZeroDivisionError as e:
    print(f"Erreur : {e}")
