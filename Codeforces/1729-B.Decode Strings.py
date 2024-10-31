def decode():
    l = int(input())
    s = input()
    ans = ''
    i = l - 1
    while i > -1:
        if s[i] != '0':
            ans += chr(96 + int(s[i]))
            i -= 1
        if s[i] == '0' and i >= 2:
            a = s[i - 2:i]
            ans += chr(96 + int(a))
            i -= 3

    return ans[::-1]

t = int(input())
for i in range(t):
    print(decode())