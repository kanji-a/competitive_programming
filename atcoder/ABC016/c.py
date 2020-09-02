import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, M = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        A, B = LI_()
        G[A].append(B)
        G[B].append(A)

    ans = [0] * N
    for i in range(N):
        que = collections.deque([i])
        dist = [INF] * N
        dist[i] = 0
        while que:
            c = que.popleft()
            for n in G[c]:
                if dist[n] > dist[c] + 1:
                    que.append(n)
                    dist[n] = dist[c] + 1
                    if dist[n] == 2:
                        ans[i] += 1

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
