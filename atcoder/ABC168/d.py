import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()


def resolve():
    N, M = LI()
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    que = collections.deque()
    que.append(0)
    dist = [INF]*N
    dist[0] = 0
    ans = [-1]*N
    while que:
        room_c = que.popleft()
        for room_n in G[room_c]:
            if dist[room_n]>=INF:
                que.append(room_n)
                dist[room_n] = dist[room_c] + 1
                ans[room_n] = room_c
    # print('dist', dist)
    # print('ans', ans)
    if -1 in ans[1:]:
        print('No')
    else:
        print('Yes')
        for i in ans[1:]:
            print(i+1)

if __name__ == '__main__':
    resolve()