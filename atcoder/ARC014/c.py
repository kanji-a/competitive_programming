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
    S = SS()

    # RxBの場合、次にRかBが来たら同じ色の側に入れると1減らせる
    # 次にGが来たら、1個先を見てGGだったら同じ側に連続で入れて個数維持
    # GRだったら右にG左にRで個数維持、GBだったら逆で同じ
    # この戦略を取ることで、筒の中は常に全部色違いで3個以内になる
    # つまり、同じ色のボールを全て打ち消すことができていることになる
    cnt = collections.Counter(S)
    ans = sum([v % 2 for _, v in cnt.items()])
    print(ans)

if __name__ == '__main__':
    resolve()
