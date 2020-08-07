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
    N, K = LI()
    A = LI()

    # 最大の長さがxになるような切断回数
    def cut_num(x):
        ret = sum([math.ceil(i / x) - 1 for i in A])
        return ret

    ng = 0
    ok = max(A)
    while abs(ok-ng)>10**(-6):
        m = (ng+ok)/2
        if cut_num(m) <= K:
            ok = m
        else:
            ng = m

    print(math.ceil(ok))

if __name__ == '__main__':
    resolve()
