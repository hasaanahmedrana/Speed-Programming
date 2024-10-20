def image():
    n=int(input(''))
    for i in range(n):
        inp1=input('')
        inp2=input('')
        inp=inp1+inp2
        s=set(inp)
        print(len(s)-1)
image()