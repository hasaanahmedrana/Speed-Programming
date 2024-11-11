from collections import defaultdict
table  = defaultdict(int)
for _ in range(int(input())):
    x = input()
    table[x] +=1
print(max(table, key=table.get))
