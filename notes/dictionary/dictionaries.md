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

**`dict.fromkeys(keys, value)`** — create a dictionary from a list of keys with a default value:

```python
keys = ["Masala", "Ginger", "Lemon"]

dict.fromkeys(keys, "Delicious")
# → {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
```

Every key gets the same default value.

**Passing `keys` as value too:**
```python
dict.fromkeys(keys, keys)
# → {'Masala': ['Masala','Ginger','Lemon'], 'Ginger': [...], 'Lemon': [...]}
```

Every key's value becomes the entire keys list — same list object assigned to all. Not very useful practically, but shows how `fromkeys` works.