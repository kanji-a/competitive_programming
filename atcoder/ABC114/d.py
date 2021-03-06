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

def primeFactorization(n):
    ans = []
    temp = n
    while temp%2 == 0:
        ans.append(2)
        temp //= 2
    for i in range(3, int(n**0.5)+1, 2):
        while temp%i == 0:
            ans.append(i)
            temp //= i
    if temp > 1:
        ans.append(temp)
    return collections.Counter(ans)

def resolve():
    N = I()

    # N!の素因数を求める
    pf_N_fact = collections.Counter()
    for i in range(1, N + 1):
        pf = primeFactorization(i)
        for k, v in pf.items():
            pf_N_fact[k] += v
    l = list(pf_N_fact.values())
    l.sort()
    pf_num = len(pf_N_fact)

    # 約数75個: 素因数の個数+1の積が75になるように組み合わせる
    # 素因数の個数を以下の組み合わせで何通り取れるかを調べる
    # (2, 4, 4), (2, 24), (4, 14), (74)
    ans = 0
    num_2 = pf_num - bisect.bisect_left(l, 2)
    num_4 = pf_num - bisect.bisect_left(l, 4)
    num_14 = pf_num - bisect.bisect_left(l, 14)
    num_24 = pf_num - bisect.bisect_left(l, 24)
    num_74 = pf_num - bisect.bisect_left(l, 74)
    ans += num_4 * (num_4 - 1) // 2 * (num_2 - 2)
    ans += num_24 * (num_2 - 1)
    ans += num_14 * (num_4 - 1)
    ans += num_74
    print(ans)

if __name__ == '__main__':
    resolve()
