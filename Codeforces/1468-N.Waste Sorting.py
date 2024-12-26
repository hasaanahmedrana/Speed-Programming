def main():
    x, y, z = map(int, input().split())
    a1, a2, a3, a4, a5 = map(int, input().split())
    x -= a1;y -= a2;z -= a3
    if x < 0 or y < 0 or z < 0: return 'NO'
    if x > a4: a4 = 0;
    else: a4 -= x;
    if y > a5: a5 = 0;
    else:a5 -= y;
    a = a4 + a5
    if a <= z:
        return 'YES'
    return 'NO'
for _ in range(int(input())):
    print(main())