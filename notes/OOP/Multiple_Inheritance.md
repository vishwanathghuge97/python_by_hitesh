## Multiple Inheritance

A class can inherit from more than one parent at the same time — getting all their methods in one place.

```python
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass    # no new code, just inheriting everything from all three
```

Just list all parents inside the parentheses — `(Battery, Engine, Car)`. That's all it takes.

```python
my_new_tesla = ElectricCarTwo("Tesla", "Model S")

print(my_new_tesla.engine_info())    # → "This is engine"   (from Engine)
print(my_new_tesla.battery_info())   # → "this is battery"  (from Battery)
```

`my_new_tesla` has access to methods from all three classes without you writing anything extra.

**Analogy:** A smartphone inherits from a phone (calls), a camera (photos), and a computer (apps) — one device, multiple capabilities.

**Simple rule:** `class Child(A, B, C)` → child gets everything from A, B, and C.