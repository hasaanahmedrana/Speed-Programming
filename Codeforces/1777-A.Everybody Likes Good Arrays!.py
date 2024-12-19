
def parity_checker(x):
    for j in range(len(x)-1):
        if (x[j]%2 and x[j+1]%2) or ((not x[j]%2) and (not x[j+1]%2)):
            return False
    return True

def main():
    l=int(input())
    x = list(map(int,input().split()))
    if parity_checker(x)==True: return 0
    c=1
    while True:
        for i in range(len(x)-1):
            if (x[i]%2 and x[i+1]%2) or ((not x[i]%2) and (not x[i+1]%2)):
                x[i]=x[i]*x[i+1]
                x.pop(i+1)
                break
        if parity_checker(x)==True: return c;
        c+=1
for _ in range(int(input())):
    print(main())

