import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    N = I()
    S = [SS() for _ in range(N)]

    cnt = collections.Counter(S)
    k_t = set()
    k_f = set()
    for i in cnt.keys():
        if i[0] == '!':
            k_f.add(i[1:])
        else:
            k_t.add(i)

    # print(k_t, k_f)
    ans = k_t & k_f
    if ans:
        print(ans.pop())
    else:
        print('satisfiable')

if __name__ == '__main__':
    resolve()
