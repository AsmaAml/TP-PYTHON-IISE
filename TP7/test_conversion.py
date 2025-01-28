import unittest
import conversion

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):

        with self.assertRaises(ValueError):
            conversion.dollars_to_dirhams(-233)

        result = conversion.dollars_to_dirhams(100)
        self.assertEqual(result , 1050.0) # pour vérifier que les résultats de la conversion sont proches des valeurs attendues avec une certaine précision
        

    def test_meters_to_kilometers(self):
        with self.assertRaises(ValueError):
            conversion.meters_to_kilometers(-23)

        self.assertEqual(conversion.meters_to_kilometers(1000), 1)
        

if __name__ == "__main__":
    unittest.main()
