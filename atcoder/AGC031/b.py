import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    C = [I() for _ in range(N)]

    # 1回以内の場合にしか答えていない
    cc = [k for k, _ in itertools.groupby(C)]
    print(cc)
    cnt = collections.Counter(cc)
    ans = (sum([i * (i - 1) // 2 % MOD for i in cnt.values()]) + 1) % MOD
    print(ans)

if __name__ == '__main__':
    resolve()
