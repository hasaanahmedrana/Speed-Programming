def main():
    l = int(input())
    x = list(map(int, input().split()))
    if l==1: return 'NO';
    if l==2 and sum(x)>2: return 'YES';
    if (len(list(set(x))) == l and l > 1): return 'YES';
    y = sum([i - 1 for i in x if i > 1])
    one = x.count(1)
    return 'YES' if y >= one else 'NO'
for _ in range(int(input())):
    print(main())