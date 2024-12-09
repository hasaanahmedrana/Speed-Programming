def main():
    s = input()
    if int(s) >= 0: return s;
    if int(s[-1]) > int(s[-2]):
        s = s[:-1]
    else:
        s = s[:-2] + s[-1]
    return s if int(s) != -0 else 0


print(main())


