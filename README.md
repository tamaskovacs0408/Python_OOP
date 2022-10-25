<h1>Python OOP</h1>

In *Python* classes can be created with the `class` keyword and the name of the `class` capitalized.
`class Item:`

Functions (`def functionName()`) that are created inside `class`es is called *methods*. The method must have a parameter called `self`. (`self` is like `this` in JavaScript)
```py
def calculate_total_price(self):
    return self.price * self.quantity
```