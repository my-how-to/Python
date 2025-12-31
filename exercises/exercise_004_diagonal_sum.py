# ============================================================
#            EXERCISE 004 — DIAGONAL SUM FROM A PATTERN
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Build a 4x4 grid where each row is [4 - i for i in range(4)],
#   then compute the sum of the main diagonal (top-left to bottom-right).
#
#   Add two versions:
#   1) With list comprehension
#   2) Without list comprehension
#
# Note:
#   The outer loop (row_index) does not change the values inside each row.
#   It only repeats the same row 4 times to form the 2D grid.
# ============================================================

# ------------------------------------------------------------
# Version 1: with list comprehension
# ------------------------------------------------------------
rows = 4
cols = 4

grid = [[cols - c for c in range(cols)] for r in range(rows)]

diag_sum = 0
for i in range(rows):
    diag_sum += grid[i][i]

print("Matrix (comprehension):", grid)
print("Main diagonal sum:", diag_sum)
# Visual:
# [
#   [4, 3, 2, 1],
#   [4, 3, 2, 1],
#   [4, 3, 2, 1],
#   [4, 3, 2, 1],
# ]
# Expected diagonal: 4 + 3 + 2 + 1 = 10

# ------------------------------------------------------------
# Version 2: without list comprehension
# ------------------------------------------------------------
rows = 4
cols = 4

grid = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(cols - c)
    grid.append(row)

diag_sum = 0
for i in range(rows):
    diag_sum += grid[i][i]

print("Matrix (loops):", grid)
print("Main diagonal sum:", diag_sum)
# Visual:
# [
#   [4, 3, 2, 1],
#   [4, 3, 2, 1],
#   [4, 3, 2, 1],
#   [4, 3, 2, 1],
# ]
# Expected diagonal: 4 + 3 + 2 + 1 = 10
