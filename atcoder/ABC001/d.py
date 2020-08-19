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
    SE = []
    for _ in range(N):
        S, E = SS().split('-')
        S = int(S) // 5 * 5
        E = ((int(E) - 1) // 5 + 1) * 5
        if E % 100 == 60:
            E += 40
        SE.append([S, E])
    SE.sort()
    # print(SE)
    
    ans = []
    tmp_s, tmp_e = SE[0]
    for s, e in SE[1:]:
        if s <= tmp_e:
            tmp_e = max(e, tmp_e)
        else:
            ans.append((tmp_s, tmp_e))
            tmp_s = s
            tmp_e = e
    ans.append((tmp_s, tmp_e))

    for s, e in ans:
        print('{:04d}'.format(s) + '-' + '{:04d}'.format(e))

if __name__ == '__main__':
    resolve()
