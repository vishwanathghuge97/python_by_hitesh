# The `for` Loop (Iterating over Sequences):

```python
# Looping through a list
teas = ["Black", "Green", "Oolong"]

for tea in teas:
    print(tea)
```

A `for` loop iterates over a fixed sequence (like a list, tuple, dictionary, or string) and executes the block of code once for each item in that collection.

---

## Looping a Specific Number of Times (`range()`):

```python
# Iterating through a range of numbers
for i in range(1, 4):
    print(i)
# Prints: 1, 2, 3
```

The `range(start, stop)` function generates a sequence of numbers starting from the `start` integer up to, but **excluding**, the `stop` integer.

---

## The `while` Loop (Condition-Based):

```python
# Repeating code until a condition becomes False
count = 1

while count <= 3:
    print(count)
    count += 1
```

A `while` loop repeatedly executes a block of code as long as its conditional expression remains `True`. It requires an explicit step to update the condition (like `count += 1`) to prevent an infinite loop.

---

## Loop Control Statements (`break` and `continue`):

```python
# break: Exits the loop immediately
for num in range(1, 6):
    if num == 3:
        break
    print(num)
# Prints: 1, 2
```

```python
# continue: Skips the rest of the current iteration
for num in range(1, 5):
    if num == 3:
        continue
print(num)
# Prints: 1, 2, 4```
**Note:** *The last code block has an indentation issue with the print statement; assuming it's intended to be inside the loop.*