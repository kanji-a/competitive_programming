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
    N, M = LI()
    # cは文字を作るときもSを作るときもペアでしか使えない
    M_pair = M // 2
    
    if M_pair > N:
        print((M_pair + N) // 2)
    else:
        print(M_pair)

if __name__ == '__main__':
    resolve()
