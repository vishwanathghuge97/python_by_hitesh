# The `yield` Keyword (Generators):

```python
# Defining a generator function
def number_generator():
    yield "First item"
    yield "Second item"
    yield "Third item"

# Initializing the generator
gen = number_generator()

for item in gen:
    print(item)
# Prints:
# First item
# Second item
# Third item
```

The `yield` keyword is used to turn a standard function into a **generator**. Unlike `return`, which completely kills the function and gives back a final value, `yield` pauses the function, sends a value out to the loop, and freezes its state. When the loop asks for the next item, the function picks up exactly where it left off.

---

## Memory Efficiency (The "Why"):

```python
# A generator that generates numbers on demand
def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1

# This does NOT store 1 million numbers in memory
big_range = count_up_to(1000000)

result1 = next(big_range)
print(result1)  # Prints: 1

result2 = next(big_range)
print(result2)  # Prints: 2
```

Instead of computing a massive list of items all at once and hoarding computer memory, a generator handles data using **lazy evaluation**. It calculates and yields only one single item at a time, exactly when you ask for it (using a loop or the `next()` function). This makes it incredibly powerful for processing massive datasets, reading giant files line-by-line, or handling infinite data streams without crashing your program.