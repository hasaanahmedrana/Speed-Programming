l=int(input())
s = [i for i in input()]
elems = {}
different = 26 - len(set(s))
count = 0
if l>26: print(-1)
else:
    for each in s:
        elems[each] = elems.get(each,0) + 1
        if elems.get(each,0) >1:
            count +=1
            elems[each] = elems.get(each) - 1
            different -= 1
    print(count) if different>=0 else print(-1)
