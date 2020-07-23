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
    E = set(LSS())
    B = SS()
    L = set(LSS())

    intersection = E & L
    match_num = len(intersection)

    if match_num == 6:
        print(1)
    elif match_num == 5:
        if B in L - intersection:
            print(2)
        else:
            print(3)
    elif 3 <= match_num <= 4:
        print(8 - match_num)
    else:
        print(0)

if __name__ == '__main__':
    resolve()
