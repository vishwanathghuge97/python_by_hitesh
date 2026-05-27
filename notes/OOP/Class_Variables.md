## Class Variables

**Concept:** A class variable belongs to the class itself, not any single object. Every object shares it.

```python
class Car:
    total_car = 0          # class variable — shared across ALL instances

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1  # increments every time any Car is created
```

**Demonstration from the video:**

```python
ElectricCar("Tesla", "Model S", "85kWh")  # calls super().__init__ → counts
Car("Tata", "Safari")                      # counts
Car("Tata", "Nexon")                       # counts

print(Car.total_car)   # → 3
```

No variables assigned — objects are created and immediately discarded. But `__init__` already ran and incremented the count. **You don't need to store the object for it to be counted.**

Output is `3` because `ElectricCar` calls `super().__init__()`, which runs `Car.__init__`, which increments `total_car`. So even Tesla counted.

**Two ways to access it:**

```python
print(Car.total_car)    # via class name — preferred
print(test.total_car)   # via instance — also works
```

**Instance variable vs Class variable:**

Instance variable — defined inside `__init__` with `self.`, belongs to each object separately. Example: `self.model`

Class variable — defined directly in class body, shared by all objects. Example: `total_car`

**Simple rule:** If every object needs its own value → instance variable. If all objects share one value → class variable.