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
    N, D, K = LI()
    LR = [LI_() for _ in range(D)]
    ST = [LI_() for _ in range(K)]

    # 貪欲法 シミュレーション 民族ごとに現在地記録
    pos = [0] * K
    for i in range(K):
        pos[i] = ST[i][0]

    ans = [0] * K

    for i in range(D):
        L, R = LR[i]
        for j in range(K):
            T = ST[j][1]
            if L <= pos[j] <= R and pos[j] != T:
                if L <= T <= R:
                    pos[j] = T
                    ans[j] = i + 1
                elif T < L:
                    pos[j] = L
                else:
                    pos[j] = R

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
