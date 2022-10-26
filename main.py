class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  
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


item1 = Item("Phone", 100, 2)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Camera", 1200, 4)

print(f"Class level attributes: {Item.__dict__}")
print(f"Instance level attributes: {item1.__dict__}")