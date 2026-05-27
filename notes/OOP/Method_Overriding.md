## Method Overriding

**Concept:** Child class redefines a method from the parent to change what it does.

`Car` has `fuel_type()` returning `"Petrol or Diesel"`. `ElectricCar` overrides it:

```python
# In Car (parent):
def fuel_type(self):
    return "Petrol or Diesel"

# In ElectricCar (child):
def fuel_type(self):
    return "Electric charge"   # same name, different behavior
```

**Result:**

```python
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())   # → "Electric charge"  (child's version)

safari = Car("Tata", "Safari")
print(safari.fuel_type())     # → "Petrol or Diesel"  (parent's version)
```

Python always uses the **most specific version** — if the child has it, child wins. Parent is only used if the child doesn't define it.

**Simple rule:** Same method name in child = override. Each object calls its own class's version.