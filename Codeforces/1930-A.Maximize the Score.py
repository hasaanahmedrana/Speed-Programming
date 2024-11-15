for _ in range(int(input())):
    x = input()
    lst = [int(i) for i in input().split()]
    lst.sort()
    lst = [lst[i] for i in range(len(lst)) if not i%2]
    print(sum(lst))