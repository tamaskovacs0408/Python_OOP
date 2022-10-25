<h1>Python OOP</h1>

In *Python* classes can be created with the `class` keyword and the name of the `class` capitalized.
`class Item:`

The first we need to create inside the `class` is the `__init__` method. (IT IS THE SAME AS THE JAVASCRIPT `contructor`). The `__init__` must have a `self` argument and we can add more args as the `class` we'd like to have. (e.g. name, price etc.)
```py
class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price
```

Functions (`def functionName()`) that are created inside `class`es is called *methods*. The method must have a parameter called `self`. (`self` is like `this` in JavaScript)
```py
def calculate_total_price(self):
    return self.price * self.quantity
```