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
    
    a = [0] * 20
    a[0] = a[1] = 100
    a[2] = 200

    for i in range(3, 20):
        a[i] = a[i-1] + a[i-2] + a[i-3]

    print(a[-1])

if __name__ == '__main__':
    resolve()
