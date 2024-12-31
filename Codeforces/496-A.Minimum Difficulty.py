def min_difficulty():
    l = int(input())
    x = list(map(int,input().split()))
    if l==3: return x[2]-x[0];
    diff = []
    for j in range(1,l-1):
        maxi =0
        y=x.copy()
        y.pop(j)
        for i in range(l-2):
            z = y[i+1]-y[i]
            if z > maxi:
                maxi = z
        diff.append(maxi)
    return min(diff)
print(min_difficulty())
