class Item:
  def __init__(self, name: str, price: float, quantity: int):
      self.name = name
      self.price = price
      self.quantity = quantity
    
  def calculate_total_price(self):
    return self.price * self.quantity


item1 = Item("Phone", 100, 2)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Camera", 1200, 4)

print(f"The name of the product is {item1.name}.")