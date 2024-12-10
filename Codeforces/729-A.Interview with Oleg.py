def main():
    l=int(input())
    s =input()
    while True:
        if '*go' in s:
           s = s.replace('*go','*',1)
        elif 'ogo' in s:
            s = s.replace('ogo','***',1)
        else:
            return s


print(main())
