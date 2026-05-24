## Python Lists

A list is an ordered, mutable collection that can hold any type of data.

**Creating a list**
```python
fruits = ["apple", "banana", "mango"]
mixed = [1, "hello", 3.14, True]
empty = []
```

**Indexing** — starts at 0
```python
fruits[0]   # "apple"
fruits[-1]  # "mango" (negative = from end)
```

**Slicing** — `list[start:stop:step]`
```python
fruits[0:2]   # ["apple", "banana"]
fruits[::-1]  # reverses the list
```

**Common methods**
```python
fruits.append("grape")      # add to end
fruits.insert(1, "kiwi")    # add at index
fruits.remove("banana")     # remove by value
fruits.pop()                # remove & return last item
fruits.sort()               # sort in place
fruits.reverse()            # reverse in place
len(fruits)                 # length

```

**`copy()` — Make an independent copy of a list:**

```python
tea_varities_copy = tea_varities.copy()
```

This creates a **separate list** with the same items. Changes to one won't affect the other.

Without `.copy()`, doing `tea_varities_copy = tea_varities` doesn't copy — both variables point to the **same list**, so changing one changes both. `.copy()` avoids that.
