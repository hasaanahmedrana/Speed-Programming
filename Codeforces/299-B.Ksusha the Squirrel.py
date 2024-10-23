def main():
    n, k = map(int, input().split())
    road = input()
    rock = 0
    for i in range(n):
        if road[i] == '#':
            rock += 1
            if rock >= k:
                print('NO')
                return
        if road[i] == ".":
            rock = 0
    print('YES')
main()