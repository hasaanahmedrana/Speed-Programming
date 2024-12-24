def main():
    s1 = list(input())
    s2 = list(input())
    x = ''
    for i in range(len(s1)):
        if s1[i] < s2[i]: return -1;
        if s1[i] == s2[i]: x += s1[i];
        if s1[i] > s2[i]: x += s2[i];
    return x
print(main())
