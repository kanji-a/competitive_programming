import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    Q = I()
    que = collections.deque()
    for _ in range(Q):
        Query = LSS()
        if Query[0] == '1':
            C, X = Query[1:]
            X = int(X)
            que.append((C, X))
        else:
            D = Query[1]
            D = int(D)
            ans = collections.Counter()
            while que:
                c, x = que.popleft()
                # Dの残りがxより小さければ戻して終わる
                if D < x:
                    que.appendleft((c, x - D))
                    ans[c] += D
                    break
                else:
                    ans[c] += x
                D -= x
            print(sum(i ** 2 for i in ans.values()))

if __name__ == '__main__':
    resolve()
