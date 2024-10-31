def check(n, k, s):
    if k == 0 or n == 1:
        return 1
    else:
        if s == s[::-1]:
            return 1
        else:
            return 2

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        s = input()
        print(check(n, k, s))
main()
