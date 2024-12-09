import unittest
from cinos_main import Drink

class TestDrink(unittest.TestCase):
    def test_get_base(self):
        drink = Drink(size="small")
        self.assertIsNone(drink.get_base())  # Default base is None

        drink.set_base("water")
        self.assertEqual(drink.get_base(), "water")

    def test_get_flavors(self):
        drink = Drink(size="medium")
        self.assertEqual(drink.get_flavors(), [])  # Default is empty list

        drink.add_flavor("cherry")
        self.assertEqual(drink.get_flavors(), ["cherry"])

    def test_get_num_flavors(self):
        drink = Drink(size="large")
        self.assertEqual(drink.get_num_flavors(), 0)  # No flavors initially

        drink.add_flavor("mint")
        drink.add_flavor("lime")
        self.assertEqual(drink.get_num_flavors(), 2)

    def test_get_total(self):
        drink = Drink(size="mega")
        self.assertEqual(drink.get_total(), 2.15)  # Base cost for mega size

        drink.add_flavor("blueberry")
        self.assertEqual(drink.get_total(), 2.15 + 0.15)

    def test_get_size(self):
        drink = Drink(size="medium")
        self.assertEqual(drink.get_size(), "medium")  # Correct size is returned

        drink.set_size("small")
        self.assertEqual(drink.get_size(), "small")


if __name__ == "__main__":
    unittest.main()
