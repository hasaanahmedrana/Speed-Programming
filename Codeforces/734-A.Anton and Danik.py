def main():
    l = int(input())
    s = input()
    if s.count('D') == s.count('A'): return 'Friendship'
    return 'Danik' if s.count('D')>s.count('A') else 'Anton'
print(main())
