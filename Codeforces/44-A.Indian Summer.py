n=int(input())
leaves_list = []
for i in range(n):
    inp = input()
    leaves_list.append(inp)
set_leaves = list(set(leaves_list))
print(len(set_leaves))