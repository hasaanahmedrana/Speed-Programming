def colors(n):
    lst = []
    for i in range(n):
        l = list(input().split())
        lst.extend(l)
    for each in lst:
        if each != "W" and each != "B" and each != "G":
            return "#Color"

    return "#Black&White"
n, m = map(int, input().split())
print(colors(n))
