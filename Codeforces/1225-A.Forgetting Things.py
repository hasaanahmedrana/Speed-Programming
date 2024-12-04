a, b = map(int,input().split())
if a == b: print(f"{a}0 {a}1");
elif b == a + 1: print(f"{a}9 {b}0");
elif a == 9 and b == 1: print("9 10");
else: print(-1);


