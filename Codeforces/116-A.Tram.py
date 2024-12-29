def main():
    entry = [0]
    all = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        entry[-1] -= x
        entry[-1] += y
        all.append(entry[0])
    return max(all)
print(main())

