import functools, itertools, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    A, B = LI()
    cum = tuple(itertools.accumulate((1, 1, 1, 1, 0, 1, 1, 1, 1, 0)))
    # print(cum)

    # 4と9を含まない数を考える方が簡単
    @functools.lru_cache
    def f(N):
        if 0 <= N <= 9:
            ret = cum[N]
        else:
            ret = (8 - cum[N%10]) * f(N // 10 - 1) + cum[N%10] * f(N // 10)
        return ret

    # print(f(B), f(A-1))
    ans = (B - (A - 1)) - (f(B) - f(A - 1))
    print(ans)

if __name__ == '__main__':
    resolve()
