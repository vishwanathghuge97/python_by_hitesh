# Multiple Conditions (`elif`):

```python
# Handling multiple mutually exclusive outcomes
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

*`elif`* stands for "else if". Python checks the conditions from top to bottom and runs *only* the first block that evaluates to `True`. Once a match is found, it skips the rest of the chain.

---

# One-Line If-Else (Ternary Operator):

```python
# Quick variable assignment based on a condition
status = "Adult" if age >= 18 else "Minor"
```

This syntax is a clean shortcut for simple assignments. It evaluates the condition in the middle; if it is `True`, it returns the value on the left, otherwise it returns the value on the right.