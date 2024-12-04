import math
n = int(input())
x = math.sqrt(n)
if x==int(x): print(int(x*4));
else:
    y = [i for i in range(1,n//2 +1) if n%i==0]
    y = [((n//i)*2)+(i*2) for i in y]
    print(min(y))
