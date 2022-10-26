class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  all = []
  def __init__(self, name: str, price: float, quantity: int):
    #Received arguments validation
      assert price >= 0, f"Price {price} is not greater or equals to 0."
      assert quantity >= 0, f"Quantity {quantity} is not greater or equals to 0."
    
    # Assign to self object
      self.name = name
      self.price = price
      self.quantity = quantity
      
    # Actions to execute
      Item.all.append(self)
    
  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate


item1 = Item("Phone", 1000, 2)
item2 = Item("Laptop", 1500, 3)
item3 = Item("Cable", 10, 4)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# print(f"Class level attributes: {Item.__dict__}")
# print(f"Instance level attributes: {item1.__dict__}")
item1.apply_discount()
print(item1.price)

print(Item.all)

for instance in Item.all:
  print(instance.name)