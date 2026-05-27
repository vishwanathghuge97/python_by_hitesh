## Private Attributes & Getter Methods

**What's new here:** `self.__brand` has double underscores — that makes it **private**.

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand    # private — hidden from outside
        self.model = model      # public — accessible directly
```

Private means you **cannot** access it directly from outside the class. Python deliberately mangles the name to block it.

```python
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.__brand)      # ❌ crashes — AttributeError
print(my_tesla.get_brand())  # ✅ works — "Tesla !"
```



```python
def get_brand(self):
    return self.__brand + " !"
```

`full_name()` also uses `self.__brand` — that's fine because it's **inside** the class, so it can access it freely.

**Why make something private?** To protect data. You don't want outside code randomly changing `__brand` directly. You control access through methods.

**Simple rule:**
- `self.model` → anyone can read/change it
- `self.__brand` → only the class itself can touch it directly; outsiders must use a method