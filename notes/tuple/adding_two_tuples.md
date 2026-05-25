**Tuple Concatenation with `+`:**

```python
more_tea = ("Herbal", "Earl Grey")
tea_types = ("Black", "Green", "Oolong")

all_tea = more_tea + tea_types
# → ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
```

`+` joins two tuples into a new one — same as string/list concatenation. The original tuples stay unchanged since tuples are **immutable**.