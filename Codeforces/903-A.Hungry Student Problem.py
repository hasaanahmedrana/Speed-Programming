def hunger():
    n = int(input())
    if n >= 13 or n == 10:
        return 'YES'
    elif n % 3 == 0 or n % 7 == 0:
        return 'YES'
    return 'NO'

for _ in range(int(input())):
    print(hunger())
