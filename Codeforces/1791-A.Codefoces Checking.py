def check():
    inp = input()
    a = 'codeforces'
    length = len(a)
    ans = 'NO'
    for i in range(length):
        if inp == a[i]:
            ans = 'YES'
            break
    return ans
def main():
    n = int(input())
    for j in range(n):
        print(check())
main()