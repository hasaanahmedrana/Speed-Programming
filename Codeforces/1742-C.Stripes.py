def main():
    ans = 'B'
    xtra = input()
    for i in range(8):
        s = input()
        if s == 'R'*8:
            ans = 'R'

    return ans
t = int(input())
for i in range(t):
    print(main())
