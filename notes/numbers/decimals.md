**Floating Point Problem & Fix**

**The Problem — float is inaccurate:**

Computers store decimal numbers in binary, and some numbers like `0.1` can't be stored perfectly. So:

```python
0.1 + 0.1 + 0.1        # → 0.30000000000000004  (not exactly 0.3!)
0.1 + 0.1 + 0.1 - 0.3  # → 5.55e-17  (should be 0, but isn't)
```

Think of it like trying to write ⅓ in decimal — you get 0.333333... and it never ends perfectly.

**Fix 1 — `Decimal` (for exact decimal math):**

```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')         # → Decimal('0.3')  ✓
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')  # → Decimal('0.0') ✓
```

Pass numbers as **strings** `'0.1'` — otherwise the float inaccuracy sneaks in again.

**Fix 2 — `Fraction` (stores as exact numerator/denominator):**

```python
from fractions import Fraction
Fraction(2, 7)  # stores it as exactly 2/7, no rounding
```

Use `Decimal` for money/finance. Use `Fraction` when you need mathematically exact fractions.