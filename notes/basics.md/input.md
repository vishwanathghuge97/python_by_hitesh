# Basic String Input:

```python
# Taking a standard text input
name = input("Enter your name: ")
print("Hello, " + name)
```

The `input()` function pauses the program and waits for the user to type. It always captures the entered data as a string (`str`), even if numbers are typed.

---

# Numeric Input (Type Casting):

```python
# Converting string input to an integer for math operations
age = int(input("Enter your age: "))
birth_year = 2026 - age
```

Since `input()` reads everything as text, you must wrap it in `int()` (for whole numbers) or `float()` (for decimals) if you need to perform calculations with the value.

---

# Multiple Inputs in One Line:

```python
# Reading multiple space-separated values at once
fresh, strong = input("Enter two flavors separated by a space: ").split()
```

Appending `.split()` breaks the user's input into separate pieces (using spaces as the default separator) and assigns them to multiple variables at the same time.