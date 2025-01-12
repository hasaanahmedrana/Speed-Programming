n = int(input())
choc = list(map(int, input().split()))
choc.sort()
choc.reverse()
coupon_n = int(input())
coupons = list(map(int, input().split()))
summ = sum(choc)
for each in coupons:
    print(summ - (choc[each - 1]))
