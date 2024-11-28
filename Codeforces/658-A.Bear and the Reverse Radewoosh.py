def main():
    n, c = map(int, input().split())
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s_1 = s_2 = 0
    t_1 = t_2 = 0
    for i in range(n):
        j = (i + 1) * -1
        t_1 += t[i]
        t_2 += t[j]
        s_1 += max(0, p[i] - (c * t_1))
        s_2 += max(0, p[j] - (c * t_2))
    if s_1 > s_2:
        print('Limak')
    elif s_1 < s_2:
        print('Radewoosh')
    else:
        print('Tie')


main()

