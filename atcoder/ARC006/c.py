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
    w = [I() for _ in range(N)]

    d = []
    for i in w:
        if d:
            idx = -1
            d_min = INF
            for j in range(len(d)):
                if d[j] >= i and d[j] < d_min:
                    d_min = d[j]
                    idx = j
            if idx == -1:
                d.append(i)
            else:
                d[idx] = i
        else:
            d.append(i)
            
    print(len(d))

if __name__ == '__main__':
    resolve()
