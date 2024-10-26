def check():
    l = int(input())
    inp = input()
    ans = []
    i = 0
    while True:
        c=inp[i]
        for k in range(i+1, l):
            if inp[k] == c:
                ans.append(c)
                i = k + 1
                break
        if i >= l:
            break
    return ''.join(ans)

def main():
    t = int(input())
    for i in range(t):
        print(check())
main()
