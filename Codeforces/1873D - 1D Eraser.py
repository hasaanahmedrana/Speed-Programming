def main():
    n,m = map(int, input().split())
    x = input()
    score = 0
    idx = 0
    while True:
        if 'B' not in x[idx:]: break;
        for i in range(idx, n):
            if x[i] == 'B':
                score += 1
                idx = i + m
                break
    return score


for _ in range(int(input())):
    print(main())

