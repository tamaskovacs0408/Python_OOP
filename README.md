<h1>Python OOP</h1>

In *Python* we can use the *f string* string formatting, which is the same (?) as *template literals* in JavaScript. Before the line we put the `f` keyword and we put the variables etc inside `{}`'s.
```py
f"The sum of 3 and 4 is {3 + 4}"
# The sum of 3 and 4 is 7
```

In *Python* classes can be created with the `class` keyword and the name of the `class` capitalized.
`class Item:`

The first we need to create inside the `class` is the `__init__` method. (IT IS THE SAME AS THE JAVASCRIPT `contructor`). The `__init__` must have a `self` argument and we can add more arguments as the `class` we'd like to have (e.g. name, price etc.). In the arguments we can set default values (`quantity=0`) so we don't have to pass it when we create a new item. Then we create new items from the class and pass the added arguments. 
```py
class Item:
  def __init__(self, name, price, quantity=0):
    self.name = name
    self.price = price

item1 = Item("Laptop", 1500)
```

Functions (`def functionName()`) that are created inside `class`es is called *methods*. The method must have a parameter called `self`. (`self` is like `this` in JavaScript)
```py
def calculate_total_price(self):
    return self.price * self.quantity
```