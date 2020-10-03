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
    N, S = LSS()
    N = int(N)

    ans = 0
    for i in range(N):
        cnt_AmT = 0
        cnt_GmC = 0
        for j in range(i, N):
            if S[j] == 'A':
                cnt_AmT += 1
            elif S[j] == 'T':
                cnt_AmT -= 1
            elif S[j] == 'G':
                cnt_GmC += 1
            elif S[j] == 'C':
                cnt_GmC -= 1
            if cnt_AmT == cnt_GmC == 0:
                ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
