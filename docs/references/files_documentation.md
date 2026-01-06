# FILE HANDLING IN PYTHON — COMPLETE GUIDE

[BACK](../README.md)

This Markdown document explains **everything about working with files in Python**, including:

* text files
* CSV
* JSON
* binary files
* encodings
* errors
* pathlib
* real‑world examples

This is the THEORY / GUIDE version.
Runnable code lives in **files_python.py**.

---

# 1. Why File Handling Matters

Python interacts with data stored outside your program: logs, configs, CSV exports, JSON APIs, reports, etc.
File handling is essential for automation, QA, scripting, and real applications.

---

# 2. Opening Files

Python uses the built‑in `open()` function.

```
open("filename", "mode", encoding="utf‑8")
```

### Common Modes

| Mode         | Meaning         | Notes                |
| ------------ | --------------- | -------------------- |
| "r"          | Read            | Default              |
| "w"          | Write           | Overwrites file      |
| "a"          | Append          | Adds to end          |
| "r+"         | Read + Write    | File must exist      |
| "x"          | Create new file | Fails if file exists |
| "b"          | Binary mode     | Use for images, PDFs |
| "t"          | Text mode       | Default              |
| combinations | e.g. "wb", "a+" | Very common          |

---

# 3. Reading Files

### Read whole file

```python
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### Read line by line

```python
for line in f:
    print(line.strip())
```

### Other read methods

| Method        | Description           |
| ------------- | --------------------- |
| `read()`      | Reads whole file      |
| `readline()`  | Reads one line        |
| `readlines()` | Returns list of lines |

---

# 4. Writing Files

Writing creates file if missing.

```python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello!\n")
```

### Append

```python
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("Another line")
```

### Write multiple lines

```python
lines = ["one\n", "two\n", "three\n"]
with open("numbers.txt", "w") as f:
    f.writelines(lines)
```

---

# 5. Using `with` (Context Manager)

`with` guarantees `.close()` even if errors occur.

```python
with open("file.txt") as f:
    ...
```

This is **best practice**.

---

# 6. File Paths: Absolute vs Relative

### Relative path

```
"example.txt"
```

### Absolute

```
"/Users/alex/Desktop/example.txt"
```

## Use `pathlib` (recommended)

```python
from pathlib import Path
p = Path("example.txt")
text = p.read_text()
```

### Check existence

```python
Path("config.json").exists()
```

---

# 7. Encoding

Always specify UTF‑8 to avoid errors.

```python
open("file.txt", "r", encoding="utf‑8")
```

Common exceptions:

* `UnicodeDecodeError`
* `UnicodeEncodeError`

---

# 8. File Handling Errors

Common exceptions:

* `FileNotFoundError`
* `PermissionError`
* `IsADirectoryError`
* `UnicodeDecodeError`

### Example

```python
try:
    with open("missing.txt") as f:
        ...
except FileNotFoundError:
    print("File not found")
```

---

# 9. Working With Binary Files

### Read binary

```python
with open("image.jpg", "rb") as f:
    data = f.read()
```

### Write binary

```python
with open("copy.bin", "wb") as f:
    f.write(b"ABC123")
```

---

# 10. Working With JSON Files

JSON is everywhere: APIs, configs, automation.

### Write JSON

```python
json.dump(data, f, indent=4)
```

### Read JSON

```python
data = json.load(f)
```

---

# 11. Working With CSV Files

Python has built‑in `csv` module.

### Write CSV

```python
writer.writerow(["Name", "Age"])
```

### Read CSV

```python
for row in reader:
    print(row)
```

## DictReader (recommended)

```python
for row in csv.DictReader(f):
    print(row["Name"])
```

---

# 12. Printing to a File

```python
print("log entry", file=f)
```

Useful for logging.

---

# 13. Real‑World File Use Cases

* Logs (automation, QA testing)
* Exporting reports
* Loading configs/settings
* Saving user input
* Reading CSV data from clients
* Writing JSON configs for your scripts
* Binary processing (images, attachments)

---

# FINAL NOTES

* Prefer `with`
* Use UTF‑8
* Use pathlib instead of raw paths
* Always handle exceptions
* CSV + JSON = most useful formats in automation & data

---

This concludes the theoretical section.
Runnable examples are located in **files_python.py**.

[BACK](../README.md)