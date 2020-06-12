import numpy as np

N, Q = map(int, input().split())
S = [input() for i in range(Q)]

follow = np.array([['N' for _ in range(N)] for _ in range(N)])

for s in S:
    type = s.split()[0]
    fromuser = int(s.split()[1])
    if type == '1':
        touser = int(s.split()[2])
        follow[fromuser-1][touser-1] = 'Y'
    elif type == '2':
        # fromuserのフォロワーを検索
        followers = []
        for i in range(N):
            if follow[i][fromuser-1] == 'Y':
                followers.append(i)
        follow[fromuser-1][followers] = 'Y'
    elif type == '3':
        followoffromuser = [i for i in range(N) if follow[fromuser-1][i] == 'Y']
        # followoffromuserのフォローしてる人を集めて、fromuserの抜く
        followfollow = []
        for i in followoffromuser:
            for j in range(N):
                if follow[i][j] == 'Y':
                    followfollow.append(j)
        followfollow = list(set(followfollow))
        if fromuser-1 in followfollow:
            followfollow.remove(fromuser-1) 
        follow[fromuser-1][followfollow] = 'Y'

for i in follow:
    print(''.join(i))