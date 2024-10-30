# line_count.py
import sys

count = 0
for line in sys.stdin:
    count += 1

# print vai para o sys.stdout
print(count)
