**String Indexing & Slicing**

**Indexing — access one character by position:**

```python
chai = "Masala Chai"
chai[0]  # → 'M'
```

Indexing starts at `0`. So `M` is at position 0, `a` at 1, and so on.


**Slicing — extract a portion using `[start:end]`:**

```python
chai[0:6]   # → 'Masala'
```

Start is **included**, end is **excluded**. So `[0:6]` gives characters at positions 0,1,2,3,4,5 — not 6.

**Slicing with step — `[start:end:step]`:**

```python
num_list = "0123456789"

num_list[:]      # → '0123456789'  (full string)
num_list[3:]     # → '3456789'     (from index 3 to end)
num_list[:7]     # → '0123456'     (from start to index 6)
num_list[0:7:2]  # → '0246'        (every 2nd character)
num_list[0:7:3]  # → '036'         (every 3rd character)
```

The third number is the **step** — how many positions to jump each time.
