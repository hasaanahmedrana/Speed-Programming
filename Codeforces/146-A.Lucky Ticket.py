
def luckeyticket():
    length = int(input())
    inp = input()
    if length % 2 != 0:
        print('NO')
        return
    else:
        for i in range(length):
            a = inp[i]
            if a != '4' and a != '7':
                print('NO')
                return
    sum1 = 0
    for j in range(length//2):
        b = int(inp[j])
        sum1 += b
    sum2 = 0
    for k in range(length // 2, length):
        c = int(inp[k])
        sum2 += c
    if sum1 == sum2: print('YES');
    else: print('NO');
luckeyticket()