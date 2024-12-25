def main():
    x = list(input())
    y = list(input())
    ans = ''
    for i in range(len(x)):
        ans += '1' if x[i]!=y[i] else '0'
    return ans
print(main())
