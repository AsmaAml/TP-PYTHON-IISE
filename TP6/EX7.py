import logging
logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message):
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        error_message = f"Erreur : Le fichier '{filename}' n'existe pas."
        log_error(error_message)  # Enregistrer l'erreur dans le fichier de log
        print(error_message)
    finally:
        print("Tentative de lecture terminée.")

fichier = r"C:\Users\user\OneDrive\Bureau\TP_Python_IISE\TP6\exemple_inexistant.txt"
read_file(fichier)
