import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    xy = [LI() for _ in range(N)]
    G = collections.defaultdict(list)
    for i, j in itertools.combinations(range(N), 2):
        G[i].append((j, (xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2)) 

    print(G)
    # Gをカットする カットする辺長の最小値が最大になるようにカットする
    # なおかつ上下の2直線にも注意 こっちが厄介?

if __name__ == '__main__':
    resolve()
