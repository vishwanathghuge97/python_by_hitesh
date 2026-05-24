**`format()` — String Formatting**

`{}` acts as a placeholder inside a string. `.format()` fills those placeholders with actual values in order.

```python
chai_type = "Masala"
quantity = 2

order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))
# → I ordered 2 cups of Masala chai
```

First `{}` gets `quantity` (2), second `{}` gets `chai_type` ("Masala") — in the same order you pass them.

Modern Python also has f-strings which do the same thing more cleanly:
```python
f"I ordered {quantity} cups of {chai_type} chai"
```