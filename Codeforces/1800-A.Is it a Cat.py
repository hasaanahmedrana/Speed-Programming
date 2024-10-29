def meow():
    l = int(input())
    s = input().lower()
    cat = [i for i in s]
    e_start = o_start = w_start = -1
    e = o = w = ""

    if l < 4:
        return "NO"

    for i in range(0, l):
        if cat[i] != "m":
            e_start = i
            e = cat[i]
            break

    for j in range(e_start, l):
        if cat[j] != e:
            o_start = j
            o = cat[j]
            break

    for i in range(o_start, l):
        if cat[i] != o:
            w_start = i
            w = cat[i]
            break

    ans = True
    for i in range(w_start, l):
        if cat[i] != "w":
            ans = False

    if cat[0] == "m" and e == "e" and o == "o" and w == "w" and ans:
        return "YES"
    else:
        return "NO"


n = int(input())
for i in range(n):
    print(meow())
