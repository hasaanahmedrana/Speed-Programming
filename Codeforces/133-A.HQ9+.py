def main():
    s = list(input())
    return 'YES' if ('H'in s or'Q' in s or '9' in s) else 'NO'


print(main())