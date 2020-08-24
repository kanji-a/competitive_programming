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
    A = [I() for _ in range(N)]

    is_ok = True

    # A[i] > iと、2以上大きくなるところがあるとダメ
    if [A[i] for i in range(N) if A[i] > i]:
        is_ok = False
    else:
        for i in range(N - 1):
            if A[i] + 1 < A[i+1]:
                is_ok = False
                break

    if is_ok:
        # 後ろの上昇列から作っていく 上昇列の最後の数字だけ回数がかかる
        ans = 0
        if N == 1:
            ans = 0
        else:
            for i in range(N - 1):
                if A[i] >= A[i+1]:
                    ans += A[i]
            ans += A[-1]

    if is_ok:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()
