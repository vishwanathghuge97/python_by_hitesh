## Python Classes — `__init__` & Attributes

**Concept:** A class is a blueprint. `__init__` runs automatically the moment you create an object from that blueprint.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

`self` refers to the specific object being created. Think of it as "this particular car." Every attribute you want the object to own must be assigned via `self.something = something`.

**Creating objects:**

```python
my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")
```

Each call to `Car(...)` creates a **separate object** with its own data. `my_car.brand` gives `"Toyota"`, `my_new_car.model` gives `"Safari"` — they don't interfere with each other.

**Analogy:** The class is a car registration form template. Each object is a filled-in form for one specific car.

**Key points to remember:**
- `__init__` = constructor. Runs on creation, never called manually.
- `self` = the object itself. Always the first parameter, never passed by you.
- `self.brand = brand` stores the value *inside* the object so you can access it later via `my_car.brand`.