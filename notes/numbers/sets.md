**Python Sets & Operations**

A **set** is a collection with **no duplicates** and **no order**.

```python
setone = {1, 2, 3, 4}
```

**`&` (AND) — common items only (intersection):**
```python
setone & {1, 3}  # → {1, 3}
```
Only items that exist in **both** sets.

**`|` (OR) — all items combined (union):**
```python
setone | {1, 3, 7}  # → {1, 2, 3, 4, 7}
```
All items from **either** set, no duplicates.

**`-` (minus) — remove matching items (difference):**
```python
setone - {1, 2, 3, 4}  # → set()
```
Removes all common items. Empty set shows as `set()`.

**Important gotcha:**
```python
type({})  # → <class 'dict'>
```
`{}` alone is a **dictionary**, not a set. To make an empty set you must write `set()`.