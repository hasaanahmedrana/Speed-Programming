def main():
    n = int(input())
    marks = list(map(int,input().split()))
    count = 0
    while True:
        x = (sum(marks)/n) + 0.5
        if x >= 5:
            return count
        count += 1
        for i in range(n):
            if marks[i] == min(marks):
                marks[i] = 5
                break
print(main())
