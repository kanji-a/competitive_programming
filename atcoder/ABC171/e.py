import sys, collections, bisect, itertools, heapq, math, copy
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
    a = LI()

    sum = 0
    for i in a:
        sum ^= i

    print(*[sum ^ i for i in a])

if __name__ == '__main__':
    resolve()
