
# Variable Keyword Arguments (`kwargs`):

```python
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="shaktiman", power="lazer")
# Prints: 
# name: shaktiman
# power: lazer

print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackaal")
# Prints: 
# name: shaktiman
# power: lazer
# enemy: Dr. Jackaal
```

Using `kwargs` allows a function to accept any number of named (keyword) arguments. The double asterisk `` collects these named inputs and packs them into a standard Python dictionary. Inside the function, you can process them using standard dictionary methods like `.items()`.