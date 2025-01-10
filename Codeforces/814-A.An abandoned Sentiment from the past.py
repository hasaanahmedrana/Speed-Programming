def main():
    n,m = map(int,input().split())
    elem = list(map(int,input().split()))
    missing = list(map(int,input().split())) ;k=0
    for i in range(n):
        if elem[i]==0:
            elem[i]=missing[k]
            k+=1
    if len(elem)==len(set(elem)) and m>1: return 'Yes';
    if len(elem)==len(set(elem)) and elem!=sorted(elem): return 'Yes';
    return 'No'
print(main())
