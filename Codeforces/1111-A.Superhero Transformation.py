def main():
    vowels = ('a','e','i','o','u')
    s = input();t=input()
    if len(s)!=len(t) : return 'NO';
    for i,j in zip(s,t):
        if (i in vowels and j not in vowels) or (i not in vowels and j in vowels):
            return 'NO'
    return 'YES'
print(main())

