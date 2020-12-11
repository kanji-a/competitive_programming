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
    N, K = LI()
    V = LI()

    # 先に取り出して、後に戻すという順番でよい
    # 取り出す深さを決めて、残った手数でいらないのを戻す
    ans = 0
    # l, r: 左、右から取る個数
    for l, r in itertools.product(range(min(N, K) + 1), repeat=2):
        if l + r <= min(N, K):
            score = 0
            minus = []
            for i in range(l):
                if V[i] >= 0:
                    score += V[i]
                else:
                    minus.append(V[i])
            for i in range(r):
                if V[N-1-i] >= 0:
                    score += V[N-1-i]
                else:
                    minus.append(V[N-1-i])
            minus.sort()
            # 残った手数で負の価値の石を戻す
            score += sum(minus[min(K-l-r, len(minus)):])
            ans = max(score, ans)

    print(ans)

if __name__ == '__main__':
    resolve()
