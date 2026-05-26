# Basic Lambda Syntax:

```python
# Syntax: lambda arguments: expression
multiply = lambda a, b: a * b

result = multiply(3, 4)
print(result)
# Prints: 12
```

A `lambda` is a small, anonymous (nameless) function squeezed onto a single line. You don't use `def`, and you don't use `return`—the result of the expression is automatically returned.

---

## The "Why" (Throwaway Functions):

While you *can* assign a lambda to a variable like `multiply` above, it defeats the purpose. Lambdas are meant to be used as quick, single-use, "throwaway" functions passed directly into other functions (like `map`, `filter`, or `sort`) without cluttering your code with `def` blocks.

---

## Using Lambda with `map()`:

```python
# Applying a quick operation to an entire list
prices = [10, 20, 30]

# map(function, iterable)
discounted = list(map(lambda price: price * 0.8, prices))

print(discounted)
# Prints: [8.0, 16.0, 24.0]
```

Instead of writing a separate `apply_discount` function, the lambda calculates 80% of the price on the fly for every single item in the list.

---

## Using Lambda with `filter()`:

```python
# Keeping only items that meet a condition
tokens = [1, 2, 3, 4, 5, 6]

# filter(condition, iterable)
evens = list(filter(lambda x: x % 2 == 0, tokens))

print(evens)
# Prints: [2, 4, 6]
```

The lambda acts as a gatekeeper. If the expression evaluates to `True` (it is an even number), the item is kept; if `False`, it is filtered out.

---

## Custom Sorting with Lambda:

```python
# Sorting a complex list
themes = [("Black", 5), ("Green", 8), ("Oolong", 6)]

# Sort strictly by the price (the second item at index 1)
teas.sort(key=lambda tea: tea[1])

print(teas)
# Prints: [('Black', 5), ('Oolong', 6), ('Green', 8)]
default,
passing a lambda to the `key` parameter tells Python exactly *what* part of the data to use for sorting.
> **Analogy:** Think of a standard `def` function like buying a reusable ceramic mug—great for long-term, repeated use. A `lambda` function is like a paper cup—you use it once for a quick task and immediately throw it away.