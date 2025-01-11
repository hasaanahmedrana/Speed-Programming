x = input()
result = ''
for i in range(len(x)):
    if i == 0:
        result += x[i].upper()
    else:
        result += x[i]
print(result)
