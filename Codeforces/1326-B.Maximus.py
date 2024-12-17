def main():
    l = int(input())
    x= list(map (int,input().split()))
    ans = [x[0]]
    p = x[0]
    for i in range(1,l):
        ans.append(x[i]+p)
        if x[i]>0: p =x[i]+p;
    return ans
z = main()
print(*z)
