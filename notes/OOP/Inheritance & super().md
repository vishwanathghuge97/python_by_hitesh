## Inheritance & `super()`

**What is it?** A child class automatically gets everything the parent has. You only add what's new.

```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)    # let Car handle brand & model
        self.battery_size = battery_size  # ElectricCar's own extra thing
```

`super()` means "go to the parent class." So `super().__init__(brand, model)` is just saying — *"Hey Car, you handle brand and model, I'll only deal with battery_size."*

**Using it:**

```python
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)       # → "Model S"  (from Car)
print(my_tesla.full_name()) # → "Tesla Model S"  (from Car)
```

`my_tesla` has everything `Car` has, plus `battery_size`.

**Analogy:** Car is a base phone. ElectricCar is the same phone with an extra camera — you don't rebuild the whole phone, just add the camera.

**Remember:**
- `class ElectricCar(Car)` → ElectricCar is the child, Car is the parent
- `super().__init__(...)` → don't repeat parent's work, delegate it
- Child gets parent's attributes + methods for free
- Only write what's **new** in the child