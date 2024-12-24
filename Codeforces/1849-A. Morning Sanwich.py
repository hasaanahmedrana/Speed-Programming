def main():
    b, c, h = list(map(int, input().split()))
    x = c + h;b -= 1
    sandwich = 1
    while True:
        if b == 0 or x == 0: return sandwich;
        else: b -= 1; x -= 1 ; sandwich += 2
for _ in range(int(input())):
    print(main())