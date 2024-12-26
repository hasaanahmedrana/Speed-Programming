def main():
    l = int(input())
    s = list(input())
    score = 0
    for i in list(set(s)):
        score += s.count(i) + 1
    return score


for _ in range(int(input())):
    print(main())