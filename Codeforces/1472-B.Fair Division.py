def main():
    l = int(input())
    candies = list(map(int, input().split()))
    if 1 in candies and 2 in candies:
        return 'YES' if sum(candies) % 2 == 0 else 'NO'
    else: return 'YES' if l % 2 == 0 else 'NO'

for _  in range(int(input())):
    print(main())
