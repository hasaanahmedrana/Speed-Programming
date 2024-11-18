for _ in range(int(input())):
    s = input()
    n = 0
    while True:
        if '10' in s:
            s = s.replace('10','',1)
            n += 1
        elif '01' in s:
            s = s.replace('01','',1)
            n +=1
        else:
            break
    if n%2:
        print('DA')
    else:
        print('NET')
