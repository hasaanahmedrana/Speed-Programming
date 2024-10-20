def long_words():
    n = int(input(''))
    for i in range(n):
        word = input('')
        length = int(len(word))
        if (length) <= 10:
            print(word)
        else:
            print(word[0], end='')
            print(length - 2, end='')
            print(word[length - 1])
long_words()