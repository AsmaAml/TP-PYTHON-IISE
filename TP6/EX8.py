import unittest
import EX6P  



# Classe de test unitaire
class TestExceptions(unittest.TestCase):

    # Test de la fonction safe_division
    def test_safe_division(self):
        # Test de la division par zéro
        with self.assertRaises(ZeroDivisionError):
            EX6P.safe_division(10, 0)
        
        # Test de la division réussie
        result = EX6P.safe_division(10, 2)
        self.assertEqual(result, 5.0) # pour vérifier que les résultats de la conversion sont proches des valeurs attendues avec une certaine précision

   

if __name__ == '__main__':
    unittest.main()
