def safe_division(a, b):
    try:
        result = a / b  
    except ZeroDivisionError:
        raise ZeroDivisionError()
    else:
        print(f"Division réussie. Résultat : {result}")
    finally:
        print("La fonction de division est terminée.")

safe_division(10, 2)  
safe_division(10, 0)  
