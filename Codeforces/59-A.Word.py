def main():
    s = input()
    upper = lower = 0
    for each in s:
        if each == each.upper():
            upper += 1;
        else:
            lower += 1
    return s.upper() if upper > lower else s.lower()


print(main())
