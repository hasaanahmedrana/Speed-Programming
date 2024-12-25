def main():
    s = int(input())
    x = list(input())
    factors = [i for i in range(2, s + 1) if s % i == 0]
    for j in factors:
        a = x[:j];b = x[j:];a.reverse()
        x = a + b
    return x


ans = main()
print(*ans, sep='')