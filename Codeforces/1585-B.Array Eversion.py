def main():
    l=int(input())
    elem = list(map(int,input().split()))
    score = 0
    elem.reverse()
    n = 0
    x = elem[0]
    for k in range(n + 1, l):
        if elem[k] > x:
            score += 1
            x = elem[k]
    return score


for _  in range(int(input())):
    print(main())