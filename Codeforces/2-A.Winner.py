def main():
    score =  dict();score_2={}
    players = []
    t = int(input())
    for _ in range(t):
        x, y = input().split()
        players.append([x, int(y)])
        score[x]=score.get(x,0)+ int(y)
    maxii = max(score.values())
    player_with_max = list(set([i for i,j in players if score.get(i)==maxii]))
    for i in range(t):
        x,y = players[i][0],players[i][1]
        score_2[x] = score_2.get(x,0)+y
        if score_2.get(x)>=maxii and  x in player_with_max:
            return x
print(main())

