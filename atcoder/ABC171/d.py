import sys, collections, bisect, itertools, heapq, math, copy
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
    N = LI()
    A = LI()
    Q = I()
    BC = [LI() for _ in range(Q)]

    cnt = collections.Counter(A)
    S = sum([k*v for k, v in cnt.items()])

    for i in BC:
        B = i[0]
        C = i[1]
        if B in cnt:
            B_num = cnt[B]
            if C in cnt.keys():
                cnt[C] += B_num
            else:
                cnt[C] = B_num
            S += (C - B) * B_num
            cnt.pop(B)
        print(S)

if __name__ == '__main__':
    resolve()
