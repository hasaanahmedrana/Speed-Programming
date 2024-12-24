def main():
    l = int(input())
    x = list(map(int, input().split()))
    parity = [2]
    for each in x:
        parity.append(each % 2)
    if parity.count(0) == 1: i = 0;
    else:i = 1;
    return parity.index(i)


print(main())