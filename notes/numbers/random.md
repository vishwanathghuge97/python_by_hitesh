**Python `random` module**

`random` is a built-in Python module for generating random numbers. You import it first:

```python
import random
```

**`random.random()`** — gives a random decimal between 0 and 1 every time you call it.

```python
random.random()  # → 0.6459763710164512
random.random()  # → 0.8317338307485483
```

**`random.randint(a, b)`** — gives a random whole number between `a` and `b`, **both included**.

```python
random.randint(1, 10)  # → 8
random.randint(1, 10)  # → 6
random.randint(1, 10)  # → 7
```
**`random.choice()` and `random.shuffle()`**

**`random.choice(list)`** — picks one random item from a list.

```python
l1 = ['lemon', 'masala', 'ginger', 'mint']
random.choice(l1)  # → 'lemon'
random.choice(l1)  # → 'ginger'
```

Every call picks a different item randomly — like picking a chit from a box.

**`random.shuffle(list)`** — randomly rearranges the entire list **in place** (modifies the original list directly, returns nothing).

```python
random.shuffle(l1)
l1  # → ['mint', 'masala', 'ginger', 'lemon']

random.shuffle(l1)
l1  # → ['mint', 'ginger', 'lemon', 'masala']
```

Like shuffling a deck of cards — same items, different order every time.

Key difference: `choice` **picks one**, `shuffle` **reorders all**.