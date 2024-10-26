def jumboextracheese():
    testcase = int(input(''))
    for i in range(testcase):
        num_slices = int(input(''))
        maximum_height = 0
        sum_base = 0
        for j in range(num_slices):
            slice = list(map(int, input().split()))
            y_axis_side = max(slice)
            if y_axis_side > maximum_height:
                maximum_height = y_axis_side
            x_axis_side = min(slice)
            sum_base += x_axis_side
        min_perimeter = 2 * (sum_base+maximum_height)
        print(min_perimeter)

jumboextracheese()