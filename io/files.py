# ============================================================
#            LESSON - FILE HANDLING
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson contains runnable, real-world examples of file
#   handling in Python. It covers reading, writing, appending,  
#   checking file existence, working with CSV and JSON, binary
#   files, exception handling, and printing to files.
#
# Contents:
#   1. Basic reading
#   2. Read line by line
#   3. Writing files
#   4. Appending to files
#   5. Check file exists
#   6. Read using pathlib
#   7. CSV — writing
#   8. CSV — reading
#   9. CSV — DictReader
#   10. JSON — writing
#   11. JSON — reading
#   12. Binary file read
#   13. Binary file write
#   14. Exceptions
#   15. print(file=...) usage
#
# ============================================================


# ================================
# 1. BASIC READING
# ================================
def read_basic():
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

# -----------------------------
# Example Output (if example.txt contains):
# Hello, world!
# Second line.
# -----------------------------


# ================================
# 2. READ LINE BY LINE
# ================================
def read_lines():
    with open("example.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# -----------------------------
# Example Output:
# Hello, world!
# Second line.
# -----------------------------


# ================================
# 3. WRITING FILES
# ================================
def write_file():
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Hello, world!\n")
        f.write("Second line.")

# -----------------------------
# After running write_file(), example.txt contains:
# Hello, world!
# Second line.
# -----------------------------


# ================================
# 4. APPENDING TO FILES
# ================================
def append_file():
    with open("example.txt", "a", encoding="utf-8") as f:
        f.write("\nAppended line.")

# -----------------------------
# After running append_file(), example.txt contains:
# Hello, world!
# Second line.
# Appended line.
# -----------------------------


# ================================
# 5. CHECK FILE EXISTS
# ================================
from pathlib import Path

def check_exists():
    print(Path("example.txt").exists())

# -----------------------------
# Example Output:
# True
# -----------------------------


# ================================
# 6. READ USING PATHLIB
# ================================
from pathlib import Path

def pathlib_read():
    p = Path("example.txt")
    if p.exists():
        print(p.read_text(encoding="utf-8"))

# -----------------------------
# Example Output:
# Hello, world!
# Second line.
# Appended line.
# -----------------------------


# ================================
# 7. WORKING WITH CSV — WRITING
# ================================
import csv

def csv_write():
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Country"])
        writer.writerow(["Alex", 32, "Moldova"])
        writer.writerow(["Maria", 28, "Romania"])

# -----------------------------
# CSV Output (data.csv):
# Name,Age,Country
# Alex,32,Moldova
# Maria,28,Romania
# -----------------------------


# ================================
# 8. WORKING WITH CSV — READING
# ================================
import csv

def csv_read():
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# -----------------------------
# Example Output:
# ['Name', 'Age', 'Country']
# ['Alex', '32', 'Moldova']
# ['Maria', '28', 'Romania']
# -----------------------------


# ================================
# 9. CSV WITH DICTREADER
# ================================
import csv

def csv_dict_read():
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["Name"], row["Age"])

# -----------------------------
# Example Output:
# Alex 32
# Maria 28
# -----------------------------


# ================================
# 10. JSON — WRITING
# ================================
import json

def json_write():
    data = {"name": "Alex", "age": 32, "city": "Chisinau"}
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# -----------------------------
# JSON Output (data.json):
# {
#     "name": "Alex",
#     "age": 32,
#     "city": "Chisinau"
# }
# -----------------------------


# ================================
# 11. JSON — READING
# ================================
import json

def json_read():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(data)

# -----------------------------
# Example Output:
# {'name': 'Alex', 'age': 32, 'city': 'Chisinau'}
# -----------------------------


# ================================
# 12. BINARY FILE READ
# ================================
def binary_read():
    with open("sample.jpg", "rb") as f:
        data = f.read(20)
        print(data)

# -----------------------------
# Example Output (first 20 bytes):
# b'\xff\xd8\xff\xe0\x00\x10JFIF...'   ← depends on file
# -----------------------------


# ================================
# 13. BINARY FILE WRITE
# ================================
def binary_write():
    with open("copy.bin", "wb") as f:
        f.write(b"ABC123XYZ")

# -----------------------------
# Output (copy.bin contains raw bytes):
# ABC123XYZ
# -----------------------------


# ================================
# 14. EXCEPTIONS
# ================================
def safe_read():
    try:
        with open("missing.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

# -----------------------------
# Example Output:
# File not found.
# -----------------------------


# ================================
# 15. PRINT TO FILE
# ================================
def print_to_file():
    with open("log.txt", "w", encoding="utf-8") as f:
        print("Logging with print()", file=f)

# -----------------------------
# After running print_to_file(), log.txt contains:
# Logging with print()
# -----------------------------


if __name__ == "__main__":
    print("Run individual functions to test file operations.")
