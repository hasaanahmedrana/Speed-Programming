def who_wins():
    n = int(input())
    l = [1] * n
    if n <= 4:
        return "Bob"
    else:
        return "Alice"

t = int(input())
for i in range(t):
    print(who_wins())
