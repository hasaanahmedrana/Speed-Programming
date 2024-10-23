months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

current_month = input('')
x = int(input())
for i in range(12):
    if current_month == months[i]:
        y = i
        break
for i in range(x):
    y += 1
    if y > 11:
        y = 0
print(months[y])
