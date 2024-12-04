n, m, a, b = map(int, input().split())
x = n * a
y = (n // m)*b+b if n % m else (n // m) * b
z = (n // m) * b + (n % m) * a
print(min(x, y, z))
