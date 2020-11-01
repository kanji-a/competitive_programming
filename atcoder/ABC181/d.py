import bisect, collections, copy, heapq, itertools, math, string, sys
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
    S = SS()

    # 下3桁が8の倍数であるような数字列を作れればYes
    S_cnt = collections.Counter(S)
    ans = 'No'
    l = [i for i in range(0, 1001, 8) if i >= 100]
    cntlist = [collections.Counter(str(i)) for i in l if str(i).count('0') == 0]
    if len(S) <= 3:
        for i in itertools.permutations(S):
            if int(''.join(i)) % 8 == 0:
                ans = 'Yes'
                break
    else:
        for i in cntlist:
            if [i[str(j)] <= S_cnt[str(j)] for j in range(1, 10)].count(False) == 0:
                ans = 'Yes'
                break

    print(ans)

if __name__ == '__main__':
    resolve()
