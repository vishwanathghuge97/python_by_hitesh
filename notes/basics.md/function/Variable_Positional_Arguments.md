# Variable Positional Arguments (`*args`):

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))
# Prints: 3

print(sum_all(1, 2, 3, 4, 5))
# Prints: 15
```

Using `*args` in a function definition allows it to accept any number of standard positional arguments. The asterisk `*` gathers all the provided values and packs them into a single tuple behind the scenes, allowing the function to handle varying amounts of data without needing a rigid parameter list.

