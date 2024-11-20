I = input;
P = print
for _ in range(int(I())):
    n = I()
    s = I().lstrip('B')
    s = s.rstrip('A')
    x = len(s) - 1
    P(x) if x >= 0 else P(0)
