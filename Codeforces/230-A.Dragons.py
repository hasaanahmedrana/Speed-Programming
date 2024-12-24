def main():
    s, n = map(int, input().split())
    x = s
    dragons=[]
    for _ in range(n):
        a, b = map(int, input().split())
        dragons.append([a, b])
    dragons.sort()
    for j in range(n):
        if dragons[j][0] < x:
            x += dragons[j][1]
        else: return 'NO'
    return 'YES'


print(main())