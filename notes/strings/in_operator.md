**`in` operator — check if a word exists in a string:**

```python
chai = "Masala Chai"

"Masala" in chai   # → True
"Masalaa" in chai  # → False
```

`in` returns `True` if the exact text is found, `False` if not. It's case-sensitive and spelling-sensitive — one extra `a` and it returns `False`.