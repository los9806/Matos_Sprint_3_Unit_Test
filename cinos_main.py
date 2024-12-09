class Drink:
    """A class for drink:
    That stores a 'base' 
    And the 'flavors' that haver been added"""

    # Valid bases and flavors for all instances
    _valid_bases = {"water", "sbrite", "pokecola", "Mr. Salt", "hill fog", "leaf wine"} 
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}     

    # Needed size and cost for each drink
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15,
    }

    # Initializer for GETTERS:
    def __init__(self, size):       # added size
        self._base = None
        self._flavors = set()   # -> 'set()' helps avoid duplicates for flavors
        self.size = None            # set the size and cost to 0
        self._cost = 0.0 
        self.set_size(size)         # sets the cost to the appropriate size

    # GETTERS to grab the different aspects for the drink:
    def get_base(self):
        return self._base
    
    # returns a 'list' for usr access
    def get_flavors(self):
        return list(self._flavors) 
    
    # Keeps a tracker for number of flavors added 
    def get_num_flavors(self):      
        return len(self._flavors)
    
    # Get the total
    def get_total(self):
        return self._cost
    
    # Get the size
    def get_size(self):
        return self.size
    
    # set the base:
    def set_base(self, base):
        if base in self._valid_bases: # Validates the base
            self._base = base
        else:
            raise ValueError(f"Invalid base: {base}. Choose a different base from {self._valid_bases}.")
        
    def add_flavor(self, flavor):       
        if flavor in self._valid_flavors:
            if flavor not in self._flavors: # Only charges for 1 instance of the same flavor 
                self._cost += 0.15
            self._flavors.add(flavor)       # Checks for a valid flavor, then adds to list (helps with duplication)
        else: 
            raise ValueError(f"Invalid flavor: {flavor}. Choose a different flavor from {self._valid_flavors}.")

    # set the falvors:    
    def set_flavors(self, flavors):
        if all(flavor in self._valid_flavors for flavor in flavors):
            new_flavors = set(flavors) - self._flavors
            self._cost += 0.15 * len(new_flavors)   # adds additional cost for flavors not already added 
            self._flavors = set(flavors)
        else:
            invalid_flavors = [flavor for flavor in flavors if flavor not in self._valid_flavors]
            raise ValueError(f"Invalid flavors: {invalid_flavors}. Choose a different flavor from {self._valid_flavors}.")

    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self.size = size # Assign the size 
            # Calculate the total cost with size base cost + flavor costs
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid size: {size}. Choose a different size from {list(self._size_costs.keys())}.")

class Food:
    """Class for food items"""

    # Defined food and price of items
    _food_prices = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tater tots": 1.70,
        "nachos": 1.90
    }

    # Defined price of additional toppings
    _topping_prices = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }

    # Getters and accessors for the different parts
    def __init__(self, food_type):
        if food_type.lower() not in self._food_prices:
            raise ValueError(f"Invalid food type.")
        self._type = food_type.lower()
        self._toppings = set()
        self._base_price = self._food_prices[self._type]

    def  get_base_price(self):
        """Accessor for the base price of the food"""
        return self._base_price

    def get_type(self):
        """Accessor for the food type"""
        return self._type

    def add_topping(self, topping):
        """Method for adding toppings"""
        if topping.lower() not in self._topping_prices:
            raise ValueError(f"Invalid topping")
        self._toppings.add(topping.lower())

    def get_toppings(self):
        """Accessor for the toppings"""
        return list(self._toppings)

    def get_num_toppings(self):
        """Method to get the number of toppings"""
        return len(self._toppings)

    def get_total_price(self):
        """Method to calculate the total food price"""
        toppings_cost = sum(self._topping_prices[topping] for topping in self._toppings)
        return self._base_price + toppings_cost

class Order: 
    """Class to contain our order items"""

    # tax rate
    _tax_rate = 0.0725

    # Initialize the class
    def __init__(self):
        self._items = []    # Create a list as a starting point 

    # GETTERS for the items and total of items
    def get_items(self):
        return self._items
    
    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return sum(
            item.get_total() if isinstance(item, Drink) else item.get_total_price()
            for item in self._items
        )

    def get_tax(self):
        total = self.get_total()
        tax = total * self._tax_rate
        return total + round(tax, 5)  # Round tax to 5 decimal places to ensure precision
    
    # Receipt Data
    def get_receipt(self):
        receipt = "Order Receipt:\n"
        total_cost = 0.0
        for i, item in enumerate(self._items):
            if isinstance(item, Drink):     
                base = item.get_base()  # Call on the Drink instance
                flavors = ", ".join(item.get_flavors())  # Call on the Drink instance
                price = item.get_total()  # Call on the Drink instance
                receipt += f"{i + 1}: Base - {base}, Flavors - {flavors}, Price: ${price:.2f}\n"
            elif isinstance(item, Food):
                food_type = item.get_type()  # Call on the Food instance
                toppings = ", ".join(item.get_toppings()) or "None"
                price = item.get_total_price()  # Call on the Food instance
                receipt += f"{i + 1}: Food - Type: {food_type}, Toppings: {toppings}, Price: ${price:.2f}\n"
        total_cost = self.get_total()
        receipt += f"Total: ${total_cost:.2f}"
        return receipt

    def add_item(self, item):
        """Method for adding an item to the order"""
        if isinstance(item, (Drink, Food)):
            self._items.append(item)
        else:
            raise ValueError("Only Drink or Food objects can be added to the order.")
        
    def remove_item(self, index):
        """Method for removing items from the order"""
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid index. Cannot remove item.")
        