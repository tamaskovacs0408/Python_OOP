from typing_extensions import assert_type


class Item:
  def __init__(self, name: str, price: float, quantity: int):
    #Received arguments validation
      assert price >= 0
      assert quantity >= 0
      assert_type(name, str)
    
    # Assign to self object
      self.name = name
      self.price = price
      self.quantity = quantity
    
  def calculate_total_price(self):
    return self.price * self.quantity


item1 = Item("Phone", 100, 2)

print(item1)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Camera", 1200, 4)

print(f"The name of the product is {item1.name}.")