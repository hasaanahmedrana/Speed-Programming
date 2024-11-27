def main():
    x = input().split()
    for i in range(len(x)):
        x[i] += x[i][0].lower()
        x[i] += 'ay'
        x[i] = x[i].replace(x[i][0],'',1)
    x[0] = x[0].capitalize()
    return x
for _ in range(int(input())):
    result = (main())
    print(*result)

