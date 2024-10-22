def blank_spaces(s, l):
    max = 0
    k = 0
    count = 0
    for i in range(k, l):
        if s[i] != 1:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    return (max)

t=int(input())
for i in range(t):
    l = int(input())
    s = list(map(int, input().split()))
    print(blank_spaces(s, l))