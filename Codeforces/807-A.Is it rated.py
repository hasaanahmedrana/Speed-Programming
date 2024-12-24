def main():
    x = []
    for _ in range(int(input())):
        a, b = map(int,input().split())
        if a != b: return 'rated';
        x.append(a)
    if x == sorted(x, reverse=True): return 'maybe';
    return 'unrated'

print(main())