**Python Dictionaries**

A dictionary stores data as **key: value** pairs.

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
```

**Accessing values:**
```python
chai_types["Masala"]        # → 'Spicy'
chai_types.get("Ginger")    # → 'Zesty'
chai_types.get("Gingery")   # → None (no error if key missing)
```

`[]` throws an error if key doesn't exist. `.get()` returns `None` safely.

**Updating a value:**
```python
chai_types["Green"] = "Fresh"   # → Green: Mild becomes Green: Fresh
```

**Looping — keys only:**
```python
for chai in chai_types:
    print(chai)
# Masala, Ginger, Green
```

**Looping — keys + values:**
```python
for chai in chai_types:
    print(chai, chai_types[chai])
# Masala Spicy, Ginger Zesty, Green Fresh
```

**Cleaner way using `.items()`:**
```python
for key, value in chai_types.items():
    print(key, value)
# same output, cleaner code
```

`.items()` gives both key and value together directly — no need to manually look up the value.