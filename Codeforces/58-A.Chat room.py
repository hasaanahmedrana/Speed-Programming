def main():
    x = input()
    word = 'hello'
    j = 0
    for i in range(len(x)):
        if x[i] == word[j]:
            j += 1
            if j == 5:
                return 'YES'
    return 'NO'


print(main())
