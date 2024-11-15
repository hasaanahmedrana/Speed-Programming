for _ in range(int(input())):
    x = input()
    track = input()
    track = track.partition('**')
    print(track[0].count('@'))

