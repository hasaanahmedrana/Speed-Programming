def lovestory(s):
    word = 'codeforces'
    count = 0
    for i in range(len(word)):
        if s[i] != word[i]:
            count += 1
    return count

t = int(input())
for i in range(t):
    s = input()
    print(lovestory(s))
