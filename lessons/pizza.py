"""Declares the Pizza class."""

class Pizza:
    """This is my class to represent pizza!"""

    size: str
    toppings: int
    gluten_free: bool


    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # Returns self


    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        return cost


    def add_toppings(self, num_toppings: int):
        """Update existing pizza order with num_toppings"""
        self.toppings += num_toppings

pie: Pizza = Pizza("medium", 2, False)
pie.add_toppings(2)
print(pie.price())
