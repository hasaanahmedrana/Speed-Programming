def main():
    s=input()
    b = input()
    l=[]
    count=0
    for i in range(len(s)):
        if s[i]!=b:
            count+=1
        else:
            l.append(count)
            count+=1
    for j in l:
        if j%2==0:
            return 'YES'
    return 'NO'
for _ in range(int(input())):
    print(main())