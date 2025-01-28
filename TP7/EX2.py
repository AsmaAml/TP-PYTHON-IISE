import os
from datetime import datetime
import math

print("Répertoire courant :", os.getcwd()) # get current working directory

print("Date et heure actuelles :", datetime.now())

number = float(input("Entrez un nombre pour calculer sa racine carrée : "))
print(f"La racine carrée de {number} = {math.sqrt(number)}")
