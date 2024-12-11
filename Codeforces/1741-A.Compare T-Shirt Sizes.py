def main():
    a, b = input().split()
    if a == b:
        return "="
    elif a[-1] == b[-1] == 'S':
        return ">" if len(a) < len(b) else "<"
    elif a[-1] == b[-1] == 'L':
        return "<" if len(a) < len(b) else ">"
    elif a[-1] == 'L' and b[-1] == 'S':
        return '>'
    elif a[-1] == 'S' and b[-1] == 'L':
        return '<'
    elif a[-1] == 'L' and b[-1] == 'M':
        return '>'
    elif a[-1] == 'M' and b[-1] == 'S':
        return '>'
    elif a[-1] == 'S' and b[-1] == 'M':
        return '<'
    elif a[-1] == 'M' and b[-1] == 'L':
        return '<'


for _ in range(int(input())):
    print(main())

