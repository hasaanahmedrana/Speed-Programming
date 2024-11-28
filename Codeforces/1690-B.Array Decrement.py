def main():
    n = int(input())
    x = (list(map(int,input().split())))
    y = (list(map(int,input().split())))
    if x==y: return 'YES';
    diff = []
    zero = []
    for i in range(n):
        if y[i]==0:
            zero.append(x[i]-y[i])
        else:
            z = x[i]-y[i]
            if z<0: return'NO';
            diff.append(z)
    if len(set(diff))>1: return 'NO'
    if diff==[] or zero==[]: return 'YES'
    for i in zero:
        if i>diff[0]: return 'NO'
    return 'YES'
for _ in range(int(input())):
    print(main())
