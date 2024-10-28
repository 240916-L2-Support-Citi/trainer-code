import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    fruits = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

value = {
    "logia": 100,
    "paramecia": 75,
    "zoan": 25 
}

sum = 0

for i in range(n):
    sum = sum + value[fruits]

print(str(sum) + " beli")