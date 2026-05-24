**Booleans in Python**

`True` and `False` are of type `bool`.

Under the hood, Python treats them as numbers — `True` is `1` and `False` is `0`:

```python
True == 1   # → True
False == 0  # → True
True + 4    # → 5  (because True = 1)
```

**`==` vs `is`:**

```python
True == 1   # → True  ✓ (same value)
True is 1   # → False ⚠️ (not the same object)
```

`==` checks if **values are equal**. `is` checks if they are the **exact same object in memory** — `True` and `1` have the same value but are different objects, so `is` returns `False`. Python also gives a warning telling you to use `==` instead.