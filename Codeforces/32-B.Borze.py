def main():
    s = input()
    i = 0;ans = ''
    while i <= len(s) - 1:
        if s[i] == '-' and s[i+1] == '-': ans += '2';i += 2;
        elif s[i] == '-' and s[i+1] == '.': ans += '1';i += 2;
        else: ans += '0'; i += 1
    return ans
print(main())