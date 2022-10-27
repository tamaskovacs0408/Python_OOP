<h1>Python OOP</h1>

**Python Virtual Environment**

To install Python modules and libraries we have to create a virtual environment (`venv`). In the terminal type the following code: `python -m venv projectFolderPath/venv` . This creates a `venv` folder in the project folder. (It's worthy to put this folder into the `.gitignore` file) After this open a new terminal and we can easily install the libraries with the `pip install libraryName` command.

In *Python* we can use the *f string* string formatting, which is the same (?) as *template literals* in JavaScript. Before the line we put the `f` keyword and we put the variables etc inside `{}`'s.
```py
f"The sum of 3 and 4 is {3 + 4}"
# The sum of 3 and 4 is 7
```
To work with `csv` files we need to import the `csv` library. (`import csv`)

In *Python* classes can be created with the `class` keyword and the name of the `class` capitalized.
`class Item:`

The first we need to create inside the `class` is the `__init__` method. (IT IS THE SAME AS THE JAVASCRIPT `contructor`). The `__init__` must have a `self` argument and we can add more arguments as the `class` we'd like to have (e.g. name, price etc.). In the arguments we can set default values (`quantity=0`) so we don't have to pass it when we create a new item. We can add the type of the arguments like this: `(name: str, price: int)`. Then we create new instances from the class and pass the added arguments. (But we can add attributes the `item1.has_numpad = True` way too)

We can "validate" the arguments (e.g. price and quantity cannot be minus) with the `assert` keyword. 
E.g. `assert price >= 0` => The price must be at least `0`. We can add a message as `AssertionError` after the "validation". (`f"Price {price} is not greater or equals to 0."`)

We created a `pay_rate` argument at the **class level**, but we can access this variable with the instance (`item1`) from the **instance level**, because it starts to find it in its level (instance level) and if it doesn't there it goes up to the class level and access it.
There is the `__dict__` attribute, that gives all the attributes from the level it's been called and convert them into a `dictionary` (object in JavaScript).

As we create the `pay_rate` and an `apply_discount` method. We access with the `self` keyword to the class level argument (pay_rate), so if we create a new instance, we can modify the pay rate. 
(E.g. `item2.pay_rate = 0.7`)

If we create an `all` list on the *class level*, we can append every instance we create (`item1`, `item2` etc) to the `all`. We have to create an `Item.all.append(self)` (all is the name of the list, we can give any name) method that append the instances to the list. (The `Item` is the name of the class, that's why its capitalized)

With the `__repr__` we can represents the `class` created instances. We add the `print(Item.all)` which gives back us the instances in the `all` list. WE can easily identify the instances of the class with this.

With the `@classmethod` we can create class methods. It takes the `cls` argument, because when we call this method, the `class` object itself will be the first argument in the background.
```py
class Item:
  pay_rate = 0.8
  all = []
  def __init__(self, name, price, quantity=0):
    assert price >= 0, f"Price {price} is not greater or equals to 0."


    self.name = name
    self.price = price

    Item.all.append(self)

    def apply_discount(self):
      self.price = self.price * self.pay_rate

    def __repr__(self):
      return f"Item('{self.name}', {self.price})"

item1 = Item("Laptop", 1500)
item2 = Item("Phone", 950)
print(Item.all) # [Item("Laptop", 1500), Item("Phone", 950)]

print(Item.pay_rate) # 0.8 access it at the class level
print(item1.pay_rate) # 0.8 access it from the instance level
print(Item.__dict__) # Gives ALL attributes from the class level (Item)
print(item1.__dict__) # Gives ALL attributes from the instance level (item1)
```

Functions (`def functionName()`) that are created inside `class`es is called *methods*. The method must have a parameter called `self`. (`self` is like `this` in JavaScript)
```py
def calculate_total_price(self):
    return self.price * self.quantity
```