

**Dictionary comprehension** — same idea as list comprehension but creates a dict:

```python
squared_num = {x: x**2 for x in range(6)}
# → {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

`x` is the key, `x**2` is the value. Syntax is `{key: value for item in iterable}`.
