def main():
    x=[]
    n=int(input())
    for _ in range(n):
        x.append(list(input()))
    while True:
        dot=0
        for i in range(n):
            for j in range(n):
                if x[i][j]=='.':
                    dot=1
                    if j+1>n-1 or j-1<0 or i+2>n-1: return 'NO'
                    if x[i+1][j-1]!='.' or x[i+1][j]!='.' or x[i+1][j+1]!='.' or x[i+2][j]!='.':
                        return 'NO'
                    else:
                        x[i][j]=x[i+1][j-1]= x[i+1][j]=x[i+1][j+1]=x[i+2][j]='#'
        if dot==0:
            return 'YES'
print(main())
