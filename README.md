<h1>Python OOP</h1>

In *Python* we can use the *f string* string formatting, which is the same (?) as *template literals* in JavaScript. Before the line we put the `f` keyword and we put the variables etc inside `{}`'s.
`f"The sum of 3 and 4 is {3 + 4}"` => The sum of 3 and 4 is 7.

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