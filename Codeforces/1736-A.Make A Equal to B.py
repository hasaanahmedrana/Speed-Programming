def make_A_equal_B():
    n = int(input())
    for i in range(n):
        length = int(input())
        array_a = list(map(int, input().split()))
        array_b = list(map(int, input().split()))
        count_1_in_a = count_1_in_b = position_differ = 0
        count_1_in_a = array_a.count(1)
        count_1_in_b = array_b.count(1)
        count_differ = abs(count_1_in_a - count_1_in_b)
        for l in range(length):
            if array_a[l] != array_b[l]:
                position_differ += 1
        if count_1_in_a == count_1_in_b:
            if position_differ == 0:
                print('0')
            else:
                print('1')
        elif count_1_in_a != count_1_in_b:
            if position_differ <= count_differ:
                print(count_differ)
            else:
                print(count_differ + 1)

make_A_equal_B()