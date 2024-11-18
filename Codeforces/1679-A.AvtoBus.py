from math import ceil
for _ in range(int(input())):
    x = int(input())
    if x%2 or x<4:
        print(-1)
    else:
        lst=[]
        if x%4==0:
            lst.append(x//4)
        if x%6==0:
            lst.append(x//6)
        if (x%6)%4==0:
            lst.append((x//6) + ((x%6)//4))
        if (x%4)%6==0:
            lst.append((x//4) + ((x%4)//6))
        if x%6==2:
            lst.append(x//6+1)
        if x%4==2:
            lst.append(x//4)
        if lst!=[]:
            print(min(lst), max(lst))
        else:
            print(-1)