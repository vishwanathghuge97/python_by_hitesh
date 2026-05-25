**Dictionary Methods — Add, Remove, Copy & Nested**

**Add a new key:**
```python
chai_types["Earl Grey"] = "Citrus"   # adds new entry
```

**Remove by key — `pop(key)`:**
```python
chai_types.pop("Ginger")  # → returns 'Zesty' and removes it
```

**Remove last item — `popitem()`:**
```python
chai_types.popitem()  # → returns ('Earl Grey', 'Citrus') and removes it
```

**Delete with `del`:**
```python
del chai_types["Green"]  # removes key, returns nothing
```


**`clear()`** — empties the entire dictionary:

```python
squared_num.clear()
squared_num  # → {}
```

**Copy:**
```python
chai_types_copy = chai_types.copy()  # independent copy
```

**Nested dictionary — dictionary inside dictionary:**
```python
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea":  {"Green": "Mild",   "Black": "Strong"}
}

tea_shop["chai"]            # → {'Masala': 'Spicy', 'Ginger': 'Zesty'}
tea_shop["chai"]["Ginger"]  # → 'Zesty'
```
