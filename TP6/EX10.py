def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
        return None

def get_integer():
    while True:
        try:
            return int(input("Veuillez saisir un entier : "))
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")

def main():
    filename = input("Veuillez entrer le chemin du fichier : ")
    content = read_file(filename)
    if content:
        print(f"Contenu du fichier :{content}")
        user_integer = get_integer()
        print(f"Vous avez saisi l'entier : {user_integer}")

if __name__ == "__main__":
    main()
