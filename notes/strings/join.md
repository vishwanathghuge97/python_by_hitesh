**`join()` — Combine a list into a string**

`join()` is the opposite of `split()`. It takes a list and joins all items into one string, with whatever separator you choose.

```python
chai_variety = ["Lemon", "Masala", "Ginger"]

"".join(chai_variety)   # → 'LemonMasalaGinger'   (no separator)
" ".join(chai_variety)  # → 'Lemon Masala Ginger'  (space)
"-".join(chai_variety)  # → 'Lemon-Masala-Ginger'  (dash)
", ".join(chai_variety) # → 'Lemon, Masala, Ginger' (comma+space)
```

The separator goes **before** `.join()` — whatever string you write there gets placed between every item.