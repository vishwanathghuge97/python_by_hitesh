**Scope — where a variable is accessible:**

```python
x = 10  # global scope — accessible everywhere

def my_func():
    y = 20  # local scope — only inside this function
    print(x)  # ✅ can access global
    print(y)  # ✅ works

print(y)  # ❌ NameError — y doesn't exist outside
```

Python looks for variables in this order: **local → enclosing → global → built-in** (called LEGB rule).

**Closure — a function that remembers variables from its enclosing scope:**

```python
def outer():
    message = "Hello"

    def inner():
        print(message)  # remembers 'message' even after outer() finishes

    return inner

my_func = outer()
my_func()  # → Hello
```

`outer()` has finished running, but `inner()` still remembers `message`. That "remembering" is a closure.

Think of it like this — `inner` carries a backpack with `message` inside it, even after `outer` is gone.

**Real use case:**
```python
def multiplier(n):
    def multiply(x):
        return x * n   # remembers n
    return multiply

double = multiplier(2)
double(5)   # → 10
double(10)  # → 20
```

Each call to `multiplier()` creates a new closure with its own `n`.