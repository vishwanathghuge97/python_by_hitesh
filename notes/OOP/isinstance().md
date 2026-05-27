## `isinstance()`

Checks whether an object is an instance of a given class. Returns `True` or `False`.

```python
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))          # → True
print(isinstance(my_tesla, ElectricCar))  # → True
```

Both are `True` because `ElectricCar` inherits from `Car`. So `my_tesla` is technically both — it's an `ElectricCar`, and since `ElectricCar` is a `Car`, it's a `Car` too.

**Analogy:** A Tesla is an electric car. An electric car is still a car. So asking "is this a car?" → yes. "Is this an electric car?" → also yes.

**Simple rule:** `isinstance(obj, Class)` → True if the object is that class **or any of its parents**.