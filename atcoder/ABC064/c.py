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
    a = LI()

    color = [0] * 9
    for i in a:
        if 0 <= i < 400:
            color[0] += 1
        elif 400 <= i < 800:
            color[1] += 1
        elif 800 <= i < 1200:
            color[2] += 1
        elif 1200 <= i < 1600:
            color[3] += 1
        elif 1600 <= i < 2000:
            color[4] += 1
        elif 2000 <= i < 2400:
            color[5] += 1
        elif 2400 <= i < 2800:
            color[6] += 1
        elif 2800 <= i < 3200:
            color[7] += 1
        else:
            color[8] += 1
    
    ans_min = len([i for i in color[:8] if i > 0]) 
    if ans_min == 0:
        print(1, color[8])
    else:
        print(ans_min, ans_min + color[8])

if __name__ == '__main__':
    resolve()
