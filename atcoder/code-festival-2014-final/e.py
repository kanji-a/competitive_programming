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
    R = LI()

    diff = [R[i+1] - R[i] for i in range(N - 1) if R[i+1] - R[i] != 0]
    # print(diff)
    
    c = 0
    for i in range(len(diff) - 1):
        if diff[i] * diff[i+1] <= -1:
            c += 1

    if c == 0:
        print(0)
    else:
        print(c + 2)

if __name__ == '__main__':
    resolve()
