def main():
    l = int(input())
    s = input()
    x = min(s.count('0'),s.count('1'))
    return l - (x * 2)
print(main())
