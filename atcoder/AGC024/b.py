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
    P = [I() for _ in range(N)]

    # Pの最長連続増加部分列以外のところを動かす回数が答え
    # 最長連続増加部分列は、各数字を昇順に並べてP内のインデックスを見ればよい
    enum_P = [(i, e) for e, i in enumerate(P)]
    enum_P.sort()
    # print(enum_P)

    cis = []
    tmp = []
    for i in range(N):
        tmp.append(enum_P[i][1])
        if i < N - 1 and enum_P[i][1] > enum_P[i+1][1]:
            cis.append(tmp)
            tmp = []
    cis.append(tmp)

    ans = N - max([len(i) for i in cis])
    print(ans)

if __name__ == '__main__':
    resolve()
