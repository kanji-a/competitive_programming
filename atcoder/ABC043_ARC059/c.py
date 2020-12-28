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
    N = I()
    a = LI()

    # 書き換え後の値をnumとすると、コストの式はnumの下に凸の2次関数
    # 下に凸なので、コスト最小になる書き換え後の整数はnumに近いどちらかの整数
    num = sum(a) // N
    ans = min([sum([(j - (num + i)) ** 2 for j in a]) for i in range(2)])

    print(ans)

if __name__ == '__main__':
    resolve()
