
**Replace a slice:**
```python
tea_varities = ['Black', 'Green', 'Oolong', 'White']

tea_varities[1:2] = ["Lemon"]   # replaces 'Green' with 'Lemon'
# → ['Black', 'Lemon', 'Oolong', 'White']
```
**Slice Assignment — Insert & Delete**

**`[1:1]` — same start and end = empty slice (nothing selected):**
```python
tea_varities[1:1]  # → []
```

**Insert items without replacing anything:**
```python
tea_varities[1:1] = ["test", "test"]
# ['Black', 'test', 'test', 'green', 'Masala', 'White']
```

Since `[1:1]` selects nothing, assigning to it just **inserts** at that position without removing anything.

**Delete a slice:**
```python
tea_varities[1:3] = []
# → ['Black', 'green', 'Masala', 'White']
```

Assigns an empty list to that slice — removes those items.

So the pattern is simple — assign a list to insert/replace, assign `[]` to delete.
