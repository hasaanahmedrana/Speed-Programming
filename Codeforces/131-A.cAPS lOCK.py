def main():
    s = input();
    if s == s.upper():
        return s.lower()
    if s[1:] == s[1:].upper():
        return s.capitalize()
    return s
print(main())



