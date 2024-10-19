def main():
    n = int(input())
    l = [0]
    for i in range(1, n + 1):
        l.append(i)
    while True:
        for i in range(len(l)):
            l[i] += i
            if (sum((l)) % n == 0):
               return l[1:]
t=int(input(''))
for i in range(t):
    ans = (main())
    print(*ans, sep=' ')