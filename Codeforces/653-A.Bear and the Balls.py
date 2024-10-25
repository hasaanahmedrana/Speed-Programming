def main():
    ans = "YES"
    num = int(input())
    sizes = list(map(int, input().split()))
    set_sizes = set(sizes)
    distinct_sizes = list(set_sizes)
    for i in range(len(distinct_sizes)):
        a = distinct_sizes[i]
        count = 0
        for j in range(len(distinct_sizes)):
            if distinct_sizes[j] > a and abs(a - distinct_sizes[j]) == 1:
                count += 1
            if distinct_sizes[j] > a and abs(a - distinct_sizes[j]) == 2:
                count += 1
            if count == 2:
                print(ans)
                return
    ans="NO"
    print(ans)
main()