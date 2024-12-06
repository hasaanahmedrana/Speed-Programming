def main():
    x = input()
    word = 'abc'
    for i in range(3):
        if x[i] == word[i]:
            return 'YES'
    return 'NO'


for _ in range(int(input())):
    print(main())


