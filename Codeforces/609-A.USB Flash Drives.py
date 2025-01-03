def main():
    n = int(input())
    file = int(input())
    usb = []
    for i in range(n):
        x = usb.append(int(input()))
    usb.sort();
    usb.reverse()
    count = 1
    for i in range(n):
        if file <= usb[i]:
            return count
        else:
            file -= usb[i]
            count+=1
print(main())
