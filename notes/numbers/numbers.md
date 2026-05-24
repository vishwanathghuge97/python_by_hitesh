
>>> math.trunc(-2.8)
-2   
nearest closet to zero means 



**Binary** — only uses `0` and `1` (base 2)
**Octal** — uses `0` to `7` (base 8)
**Hexadecimal** — uses `0` to `9` and `A` to `F` (base 16)

These are just **different ways to write the same number.** Like how 12 rupees = one 10-rupee note + two 1-rupee coins — same value, different form.

In Python, you tell it which system you're using with a prefix:

```python
0b1000   # "0b" means binary  → equals 8
0o20     # "0o" means octal   → equals 16
0xFF     # "0x" means hex     → equals 255
```

And if you want to **convert**:

```python
bin(8)   # gives you '0b1000'  → 8 in binary
int('1000', 2)  # reads '1000' as binary → gives back 8
```
