**Defining and Calling a Function:**

```python
# Defining a simple function
def greet_user(name):
    print("Hello, " + name + "!")

# Calling the function
greet_user("Alice")

```

The `def` keyword tells Python you are defining a function. The variable inside the parentheses (`name`) is a **parameter**, which acts as a placeholder for the actual data passed into the function when you call it.

---

**Returning Values:**

```python
# Returning a value to the caller
def square_number(number):
    return number ** 2

result = square_number(4)  # result now holds the value 16

```

The `return` statement sends a value back to the line of code that called the function and exits the function immediately. If a function doesn't have an explicit `return` statement, it automatically returns `None`.

---

**Default Parameters:**

```python
# Setting a fallback value for a parameter
def make_tea(tea_type="Green"):
    print("Brewing a cup of " + tea_type + " tea.")

make_tea()          # Uses default -> "Brewing a cup of Green tea."
make_tea("Black")   # Overrides default -> "Brewing a cup of Black tea."

```

You can assign a default value to a parameter in the function definition. If the caller doesn't provide an argument for that parameter during the function call, Python smoothly falls back to the default value.