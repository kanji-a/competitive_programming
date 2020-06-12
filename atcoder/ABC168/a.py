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

    s = N[-1]
    if s=='3':
        print('bon')
    elif s in ['0', '1', '6', '8']:
        print('pon')
    else:
        print('hon')

if __name__ == '__main__':
    resolve()