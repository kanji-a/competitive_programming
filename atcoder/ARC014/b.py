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
    W = [SS() for _ in range(N)]

    last_c = W[0][-1]
    word = {W[0]}
    ans = 'DRAW'
    for i in range(1, N):
        if W[i][0] != last_c or W[i] in word:
            if i % 2 == 0:
                ans = 'LOSE'
            else:
                ans = 'WIN'
            break
        last_c = W[i][-1]
        word.add(W[i])

    print(ans)

if __name__ == '__main__':
    resolve()
