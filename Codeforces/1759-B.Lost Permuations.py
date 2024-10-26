def lost_permutation():
    m, s = map(int, input().split())
    l = list(map(int, input().split()))
    j = sum_j = 1
    while sum_j <= s:
        if j > s:
            break
        if j not in l:
            l.append(j)
            sum_j += j
        j += 1
    maxi = max(l)
    if sum_j-1 != s:
        return "NO"


    if len(l) == maxi and len(l)!=1:
        return "YES"
    return "NO"


t = int(input())
for i in range(t):
    print(lost_permutation())