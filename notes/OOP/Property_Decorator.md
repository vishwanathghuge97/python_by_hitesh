## `@property` — Property Decorator

Normally a method needs parentheses to call:
```python
my_car.model()   # method — needs ()
my_car.model     # attribute — no ()
```

`@property` bridges that gap — it lets you write a method but access it like an attribute (no parentheses needed).

**Why does that matter?** Because you want the clean look of attribute access but the control of a method — so you can hide the real variable and decide what gets returned.

```python
class Car:
    def __init__(self, brand, model):
        self.__model = model      # private — hidden from outside

    @property
    def model(self):
        return self.__model       # exposed safely through property
```

Now `my_car.model` silently calls the method. The caller doesn't even know it's a method — it just looks like reading an attribute.

```python
my_car = Car("Tata", "Safari")
print(my_car.model)      # ✅ → "Safari"  (reads via property)
my_car.model = "City"    # ❌ blocked  (no setter defined)
```

Since nobody can touch `__model` directly, and no setter is written, it becomes **read-only** — you can read it, you can't change it.

**Two things `@property` gives you:**
- Access a method like a plain attribute (no parentheses)
- Control over reading — and optionally writing — a private attribute

**Simple rule:** `@property` = method disguised as an attribute, giving you control over how data is accessed.