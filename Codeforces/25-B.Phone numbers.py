n= int(input())
s = input()
lst = []
if n<=3:
    lst =[s]
elif n<=5:
    lst = [s[:n//2],s[n//2:]]
elif n<10:
    lst += [s[:n//3], s[n//3:(2*n)//3] ,s[(2*n)//3:]]
else:
    lst =[s[i]+s[i+1] for i in range(0,n-1,2)]
    if n%2:
        lst.pop()
        lst += [s[n-3:]]
print(*lst,sep='-')
