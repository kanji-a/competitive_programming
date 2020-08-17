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

    # 0をA_nにすると1ケースWAが減る謎
    A_p = [i for i in A if i >= 0]
    A_p.sort()
    A_n = [i for i in A if i < 0]
    A_n.sort()

    if A_p and A_n:
        # 正の数を1個以外負の数から引く
        # 残した正の数から負の数を全部引く
        print(sum(A_p) - sum(A_n))

        tmp = A_n[0]
        for i in range(1, len(A_p)):
            print(tmp, A_p[i])
            tmp -= A_p[i]
        print(A_p[0], tmp)
        tmp = A_p[0] - tmp
        for i in range(1, len(A_n)):
            print(tmp, A_n[i])
            tmp -= A_n[i]

    elif A_p and not A_n:
        # 正の数しかない場合、最小値から他の数字を1個残して引いたものを、残った数字から引く
        print(sum(A_p[1:]) - A_p[0])

        tmp = A_p[0]
        for i in range(1, len(A_p) - 1):
            print(tmp, A_p[i])
            tmp -= A_p[i]
        print(A[-1], tmp)

    elif not A_p and A_n:
        # 負の数しかない場合、最大値から他の数字を全部引く
        print(A_n[-1] - sum(A_n[:-1]))

        tmp = A_n[-1]
        for i in range(len(A_n) - 1):
            print(tmp, A_n[i])
            tmp -= A_n[i]

if __name__ == '__main__':
    resolve()
