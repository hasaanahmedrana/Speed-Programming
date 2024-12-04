def main():
    n=int(input())
    x=list(map(int,input().split()))
    y=[i%3 for i in x]
    c=n//3;score=0
    c_1=y.count(1)
    c_0=y.count(0)
    c_2=y.count(2)
    while True:
        if c_0==c_1==c_2==c: return score;
        elif c_0>c:c_1+=(c_0-c);score+=(c_0-c);c_0=c;
        elif c_2>c: c_0+=(c_2-c);score+=(c_2-c);c_2=c;

        elif c_1>c: c_2+=(c_1-c);score+=(c_1-c);c_1=c;
for _ in range(int(input())):
    print(main())

