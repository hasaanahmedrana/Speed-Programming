def main():
    s = list(input().lower())
    vowels = ('a', 'e', 'i', 'u', 'o', 'y')
    s = [i for i in s if i not in vowels]
    print('.', end='')
    print(*s, sep='.')


main()

