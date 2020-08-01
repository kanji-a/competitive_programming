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
    N, A, B, C, D = LI()
    A -= 1
    B -= 1
    C -= 1
    D -= 1
    S = SS()

    ## 移動経路に2連続以上の岩があったらダメ
    if '##' in S[A:C+1] or '##' in S[B:D+1]:
        print('No')
    else:
        ## ふぬけ君を先に移動させればいい
        if C < D:
            print('Yes')
        ## ふぬけ君を飛び越えられる瞬間が存在すればいい
        else:
            # どこかに3以上の隙間があること
            if '...' in S[B-1:D+2]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    resolve()
