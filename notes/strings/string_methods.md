**String Methods — Complete Notes**

**`lower()` / `upper()`** — change case, original unchanged:
```python
chai = "Masala Chai"
chai.lower()  # → 'masala chai'
chai.upper()  # → 'MASALA CHAI'
```

**`strip()`** — removes spaces from both sides:
```python
chai = "   Masala Chai   "
chai.strip()  # → 'Masala Chai'
```

**`replace(old, new)`** — replaces a word, original unchanged:
```python
chai = "Lemon Chai"
chai.replace("Lemon", "Ginger")  # → 'Ginger Chai'
```

**`split(separator)`** — breaks string into a list:
```python
chai = "Lemon, Ginger, Masala, Mint"
chai.split()         # → ['Lemon,', 'Ginger,', 'Masala,', 'Mint']  (splits on space)
chai.split(", ")     # → ['Lemon', 'Ginger', 'Masala', 'Mint']     (splits on ", " cleanly)
```

**`find(word)`** — returns index of first match, `-1` if not found:
```python
chai = "Masala Chai"
chai.find("Chai")   # → 7   (found at index 7)
chai.find("chai")   # → -1  (case sensitive, not found)
```

**`count(word)`** — counts how many times a word appears:
```python
chai = "Masala Chai Chai Chai"
chai.count("Chai")  # → 3
```

All these methods **never modify the original string** — they always return a new result.