def gender():
    inp = input('')
    length = len(inp)
    string = '_'
    distinct_alpha = 0
    for i in range(length):
        length_of_s = len(string)
        a = inp[i]
        for k in range(length_of_s):
            b = string[k]
            count = 0
            if b != a:
                count += 1
            if b == a:
                count = 0
                break
        if count > 0:
            distinct_alpha += 1
        string = string + a
    if distinct_alpha % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
gender()