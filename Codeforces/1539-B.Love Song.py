def love_story(x):
    a, b = map(int, input().split())
    a -= 1
    return x[b]-x[a]


def main():
    l, n = map(int, input().split())
    song = list(input())
    for i in range(l):
        song[i] = ord(song[i])-96
    x = [0]
    for j in range(l):
        y = x[-1] + song[j]
        x.append(y)
    for _ in range(n):
        print(love_story(x))
main()
