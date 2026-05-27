## Static Methods (`@staticmethod`)

**Concept:** A method that belongs to the class but doesn't need any object data — no `self`.

```python
@staticmethod
def general_description():
    return "Cars are means of transport"
```

Call it via instance or class directly — both work:

```python
print(my_car.general_description())   # → "Cars are means of transport"
```

**Why `@staticmethod`?** Without it, Python auto-passes `self` when called on an instance. If your method has no `self` parameter, it crashes:

```python
# Without @staticmethod → crash
TypeError: takes 0 positional arguments but 1 was given
```

`@staticmethod` tells Python: *don't pass self automatically.*

**When to use it?** When the logic relates to the class but is true for all objects equally — no specific object data needed. "Cars are means of transport" applies to every car, so no `self` required.

**Simple rule:** Method doesn't use `self` anywhere inside it → use `@staticmethod`.