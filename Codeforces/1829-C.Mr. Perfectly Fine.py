def main():
    t = int(input())
    l_01 = []
    l_10 = []
    l_11 = []
    for i in range(t):
        n, m = map(int, input().split())
        if m==1 and (not l_01):
            l_01 = [n]
        elif m==10 and (not l_10):
            l_10 = [n]
        elif m==11 and (not l_11):
            l_11 = [n]
        elif m==1 and n < l_01[0]:
            l_01 = [n]
        elif m==10 and n < l_10[0]:
            l_10 = [n]
        elif m==11 and n < l_11[0]:
            l_11 = [n]
    if (l_01 == [] or l_10 == []) and l_11 == []:
        return -1;
    elif (l_01 == [] or l_10 == []) and l_11 != []:
        return l_11[0];
    elif l_01 == [] and l_10 == l_11 != []:
        return min(l_10[0], l_11[0]);
    elif l_10 == [] and l_01 == l_11 != []:
        return min(l_01[0], l_11[0]);
    elif (l_01!=[] and l_10 != []) and l_11 == []:
        return l_01[0] + l_10[0]
    return min(l_01[0] + l_10[0], l_11[0])

for _ in range(int(input())):
    print(main())
