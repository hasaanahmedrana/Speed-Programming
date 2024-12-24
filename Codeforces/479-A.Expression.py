def main():
    x=[int(input()) for i in range(3)]
    a = sum(x)
    b= x[0]*x[1]*x[2]
    c= (x[0]+x[1])*x[2]
    d= x[0]*(x[1]+x[2])
    return max(a,b,c,d)
print(main())
