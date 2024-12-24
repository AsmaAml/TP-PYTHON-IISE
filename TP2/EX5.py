# Classe de base
class Animal:
    def faire_du_bruit(self):
        return "Cet animal fait un bruit indéfini."

# Sous-classe Chien
class Chien(Animal):
    def faire_du_bruit(self):
        return "Le chien aboie : Woof Woof!"

# Sous-classe Chat
class Chat(Animal):
    def faire_du_bruit(self):
        return "Le chat miaule : Miaou!"

# Tester les sous-classes
chien = Chien()
chat = Chat()
animal = Animal()

print(chien.faire_du_bruit())  # Appelle la méthode spécifique à Chien
print(chat.faire_du_bruit())   # Appelle la méthode spécifique à Chat
print(animal.faire_du_bruit()) # Appelle la méthode par défaut d'Animal
