

**Raw string `r"..."` — treats backslash as plain text:**
```python
chai = r"Masala\nChai"
print(chai)  # → Masala\nChai  (no newline, printed literally)
```

Putting `r` before the string tells Python — ignore all escape sequences, treat `\` as just a backslash character.

**Real-world use — Windows file paths:**
```python
chai = "c:\user\pwd"   # ❌ SyntaxError — \u is treated as unicode escape
chai = r"c:\user\pwd"  # ✅ works perfectly
chai = "c:\\user\\pwd" # ✅ also works — double backslash escapes it
```

Windows paths use `\` which conflicts with Python's escape sequences. Fix it with either `r""` or `\\`.