def main():
    n =int(input())
    x= [2,4]
    for _ in range(n-2):
        x.append(x[-1]+3)
    return x


for _ in range(int(input())):
    result = main()
    print(*result)
