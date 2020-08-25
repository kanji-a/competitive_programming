import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()
    A = LI()

    ans = 0
    A.reverse()
    # nodes = A[0]
    # ans += nodes
    # for i in range(1, N):
    #     nodes = (nodes+1)//2+A[i]
    #     ans += nodes
    #     print(nodes, ans)
    # nodes = (nodes+1)//2+A[-1]
    # if nodes!=1:
    #     ans = -1
    # else:
    #     ans += nodes
    # print(ans)

    # なるべく別の枝で max頂点数越えたらアウト
    nodes = 0
    for i in range(0, N+1):
        nodes += A[i]
        # if nodes>2**(N-i):
        #     ans = -1
        #     break
        nodes = min(2**(N-i), nodes)
        ans += nodes
        # print(ans, nodes)

    print(ans)


if __name__ == '__main__':
    resolve()
