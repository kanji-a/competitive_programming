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
    N = I()
    A = LI()
    A.sort()

    # Aがあるサイズ以上であればその色にできる
    # 自分より小さいやつを全部吸収した後で、自分より大きいやつを全部吸収できるか
    A_cum = [0] * (N + 1)
    for i in range(N):
        A_cum[i+1] = A_cum[i] + A[i]

    l = [A_cum[i] * 2 >= A[i] for i in range(1, N)]
    l.reverse()
    if False in l:
        print(l.index(False) + 1)
    else:
        print(N)

if __name__ == '__main__':
    resolve()
