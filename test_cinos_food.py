import unittest
from cinos_main import Food

class TestFood(unittest.TestCase):

    def test_get_base_price(self):
        food = Food("hotdog")
        self.assertEqual(food.get_base_price(), 2.30)

    def test_get_type(self):
        food = Food("ice cream")
        self.assertEqual(food.get_type(), "ice cream")

    def test_get_toppings(self):
        food = Food("nachos")
        self.assertEqual(food.get_toppings(), [])  # No toppings initially
        food.add_topping("chili")
        self.assertEqual(food.get_toppings(), ["chili"])

    def test_get_num_toppings(self):
        food = Food("tater tots")
        self.assertEqual(food.get_num_toppings(), 0)
        food.add_topping("ketchup")
        food.add_topping("bacon bits")
        self.assertEqual(food.get_num_toppings(), 2)

    def test_get_total_price(self):
        food = Food("french fries")
        self.assertEqual(food.get_total_price(), 1.50)
        food.add_topping("nacho cheese")
        self.assertEqual(food.get_total_price(), 1.80)  # Includes topping cost

if __name__ == "__main__":
    unittest.main()

