class Item:
  def __init__(self, name: str, price: float, quantity: int):
    #Received arguments validation
      assert price >= 0, f"Price {price} is not greater or equals to 0."
      assert quantity >= 0, f"Quantity {quantity} is not greater or equals to 0."
    
    # Assign to self object
      self.name = name
      self.price = price
      self.quantity = quantity
    
  def calculate_total_price(self):
    return self.price * self.quantity


item1 = Item(443, -100, 2)
print(item1.name)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Camera", 1200, 4)
