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
