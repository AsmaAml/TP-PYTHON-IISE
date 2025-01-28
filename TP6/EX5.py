def process_input(user_input):
    try:
        number = int(user_input)  # Conversion en entier
        result = 10 / number  # Division par 10
        print(f"Résultat : {result}")
    except ValueError:
        print(f"Erreur : '{user_input}' n'est pas un entier valide.")
    except ZeroDivisionError:
        print(f"Erreur : Division par zéro.")

process_input("abc")  
process_input("0")    
process_input("5")    
