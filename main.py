import csv

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
    
  @classmethod
  def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
  def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone", 1000, 2)
# item2 = Item("Laptop", 1500, 3)
# item3 = Item("Cable", 10, 4)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(f"Class level attributes: {Item.__dict__}")
# print(f"Instance level attributes: {item1.__dict__}")
# item1.apply_discount()
# print(item1.price)

Item.instantiate_from_csv()
print(Item.all)
