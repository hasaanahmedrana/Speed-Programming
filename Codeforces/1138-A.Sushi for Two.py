n = int(input())
x = list(map(int, input().split()))
count_1 = count_2 = 0
ones = [];
twos = [];
value = [];
q = x[0]
for i in range(n):
    if i > 0 and x[i] != q:
        if x[i] == 1:
            if count_2 != 0:
                twos.append(count_2)
                if ones != [] and twos != []:
                    value.append(min(ones[-1], twos[-1]) * 2)
            count_2 = 0
            q = 1
        else:
            if count_1 != 0:
                ones.append(count_1)
                if ones != [] and twos != []:
                    value.append(min(ones[-1], twos[-1]) * 2)
            count_1 = 0
            q = 2
    if x[i] == 1: count_1 += 1;
    if x[i] == 2: count_2 += 1
    if i == n - 1:
        if count_1 != 0:
            ones.append(count_1)
        if count_2 != 0:
            twos.append(count_2)
        if ones != [] and twos != []:
            value.append(min(ones[-1], twos[-1]) * 2)

print(max(value))

