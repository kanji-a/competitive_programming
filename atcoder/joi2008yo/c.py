import sys
input = lambda: sys.stdin.readline().rstrip() 
import bisect as bs

def resolve():
    n = int(input())
    T = [int(input()) for _ in range(n)]

    deck = [[0]*(2*n+1), [0]*(2*n+1)]
    for i in range(1, 2*n+1):
        if i in T:
            owner = 0
        else:
            owner = 1
        deck[owner][i] = 1

    field = 0
    cnt = [n, n]
    player = 0
    while cnt[0]>0 and cnt[1]>0:
        for i in range(field+1, 2*n+1):
            if deck[player][i]==1:
                field = i
                deck[player][i] = 0
                cnt[player] -= 1
                break
        else:
            field = 0
        player = 1 - player
    print(cnt[1])
    print(cnt[0])

if __name__ == '__main__':
    resolve()
