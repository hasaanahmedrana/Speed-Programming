def main():
    s2 = input()
    s2.split()
    s = list(s2)
    for i in range(len(s)-1):
        s.pop()
        if s != s[::-1]:
            return len(s)
    return - 1

t=int(input())
for i in range(t):
    print(main())