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
    AB = [LI() for _ in range(N)]
    
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)

    score_t = 0
    score_a = 0
    for i in range(N):
        a, b = AB[i]
        if i % 2 == 0:
            score_t += a
        else:
            score_a += b

    print(score_t - score_a)

if __name__ == '__main__':
    resolve()
