def main():
    s = input()
    exceptions = ('a', 'e', 'i', 'o', 'u')
    if s[-1] not in exceptions and s[-1] != 'n': return 'NO'
    for i in range(len(s) - 1):
        if (s[i] not in exceptions and s[i] != 'n') and s[i + 1] not in exceptions:
            return 'NO'
    return 'YES'


print(main())

