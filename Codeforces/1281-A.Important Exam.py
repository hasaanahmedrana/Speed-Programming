num_student, num_ques = map(int, input().split())
list1 = [input() for i in range(num_student)]
marks = list(map(int, input().split()))
obtained_marks = 0
for i in range(num_ques):
    list2 = []
    count = [0] * 5
    for j in range(len(list1)):
        c = list1[j][i]
        list2.append(c)
        if c == "A": count[0] += 1;
        if c == "B": count[1] += 1;
        if c == "C": count[2] += 1;
        if c == "D": count[3] += 1;
        if c == "E": count[4] += 1;
    n = max(count)
    obtained_marks += marks[i]*n
print(obtained_marks)

