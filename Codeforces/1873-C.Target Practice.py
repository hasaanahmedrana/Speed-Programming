def main():
    lst = []
    score = 0
    for _ in range(10):
        lst.append(input())
    for i in range(10):
        for j in range(10):
            if lst[i][j] == "X":
                n = 1+i if i <= 4 else 9 - i + 1
                m = 1+j if j <= 4 else 9- j + 1
                score += min(n, m)
    return score


for _ in range(int(input())):
    print(main())

