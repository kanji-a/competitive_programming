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
    N = S()

    xxx = [str(i) * 3 for i in range(10)]
    if [i for i in xxx if i in N]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
