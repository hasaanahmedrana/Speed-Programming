def kefa():
    l = int(input())
    array = list(map(int, input().split()))
    points=[];count = 1
    for i in range(1,l):
        if array[i] < array[i-1]:
            points.append(count)
            count = 1
        else:
            count += 1


    points.append(count)
    return max(points)
print(kefa())
