import unittest
from cinos_main import Drink, Food, Order

class TestOrder(unittest.TestCase):

    def test_get_items(self):
        order = Order()
        self.assertEqual(order.get_items(), [])  # No items initially
        drink = Drink(size="medium")
        order.add_item(drink)
        self.assertEqual(order.get_items(), [drink])  # Items should include added drink

    def test_get_num_items(self):
        order = Order()
        self.assertEqual(order.get_num_items(), 0)
        food = Food("corndog")
        order.add_item(food)
        self.assertEqual(order.get_num_items(), 1)

    def test_get_total(self):
        order = Order()
        drink = Drink("medium")
        drink.set_base("sbrite")
        drink.add_flavor("lemon")
        food = Food("hotdog")
        food.add_topping("ketchup")
        order.add_item(drink)
        order.add_item(food)
        expected_total = drink.get_total() + food.get_total_price()
        self.assertAlmostEqual(order.get_total(), expected_total)

    def test_get_tax(self):
        order = Order()
        expected_total = order.get_total()
        expected_tax = expected_total * 0.0725  # Tax rate
        expected_total_with_tax = expected_total + round(expected_tax, 5)
        self.assertAlmostEqual(order.get_tax(), expected_total_with_tax)

    def test_get_receipt(self):
        order = Order()
        drink = Drink(size="small")
        drink.set_base("pokecola")
        drink.add_flavor("lime")
        food = Food("nachos")
        food.add_topping("chili")
        order.add_item(drink)
        order.add_item(food)
        receipt = order.get_receipt()
        self.assertIn("pokecola", receipt)
        self.assertIn("lime", receipt)
        self.assertIn("nachos", receipt)
        self.assertIn("chili", receipt)

if __name__ == "__main__":
    unittest.main()

