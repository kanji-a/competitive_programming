import bisect, collections, copy, functools, heapq, itertools, math, string, sys
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
    n, k = LI()
    n_tmp = n
    n = n_tmp * (20 // n_tmp)
    s = SS()
    s = s * (20 // n_tmp)
    d = {'R': 0, 'P': 1, 'S': 2}
    d_r = {0: 'R', 1: 'P', 2: 'S'}

    def te(i):
        return d[s[i%n]]

    # 同じRPSの並びの区間が出たら結果を使い回す
    @functools.lru_cache
    def f(l, r):
        # print(l, r)
        if r - l == 1:
            return l
        else:
            m = (l + r) // 2
            offset_l = l // n * n
            left = f(l - offset_l, m - offset_l)
            # offset_r = m // n
            right = f(m - offset_l, r - offset_l)
            # print(l, r, left, right, d_r[te(left)], d_r[te(right)])
            if (te(left) - te(right)) % 3 <= 1:
                return left
            else:
                return right

    ans = f(0, 2 ** k)
    print(s[ans])

if __name__ == '__main__':
    resolve()
