import pandas as pd

# Lire le fichier CSV et afficher les 5 premières lignes
try:
    df = pd.read_csv(r'C:\Users\user\OneDrive\Bureau\TP_Python_IISE\TP7\employees.csv')
    print(df.head())

    # Vérifier et calculer la moyenne de l'âge
    if 'Âge' in df.columns:
        print(f"\nLa moyenne de l'âge des employés est : {df['Âge'].mean()} ans") 
    else:
        print("\nLa colonne 'Âge' n'existe pas dans le fichier CSV.")

except FileNotFoundError:
    print("Erreur : Le fichier 'employees.csv' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
