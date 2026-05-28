My bad. Here:

---

**Step 1 — Nested functions**

A function inside a function. The inner function only exists inside the outer function, just like a room only exists inside a house.

outer() = house
inner() = room inside the house
street = outside all functions

```
def outer() {
    def inner() {   ← room, only accessible from inside house
    }
}

inner()  ← ERROR, street doesn't know room exists
```

---

**Step 2 — How Python reads it line by line**

1. outer() is called — you enter the house
2. Python sees def inner() — just takes a note, does NOT run it. Like reading a recipe but not cooking yet.
3. Python sees inner() call inside outer — now it runs. You're inside the house, you have the key.

The inner() call lives at house level, not inside the room itself.

---

**Step 3 — Free variable (the TV)**

The house has a variable like tv = "Sony TV". The room borrows it because room is inside the house. That borrowed variable is called a free variable. It doesn't originally belong to the room but room captures it from the house.

---

**Step 4 — The closure**

Normally when outer() finishes, everything inside dies. But if outer does return inner before dying, it gives the room a separate address. You catch it outside.

return inner = give the room's address before house dies
my_room = outer() = you on the street catch that address
my_room() = your keys to enter the room anytime

House is gone. Room is alive. TV still inside. That is a closure.

---

**Step 5 — return inner vs return inner()**

return inner = hand over the room itself, enter it later with ()
return inner() = enter the room right now and return only the result, not the room

---

**Why is it called closure?**

The inner function closes over the variable, wrapping itself around the TV and locking it inside before the house falls.