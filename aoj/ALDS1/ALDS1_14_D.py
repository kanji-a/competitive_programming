import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def contain(a, b):
    a = [ord(i) for i in a]
    b = [ord(i) for i in b]
    B = 10000007
    H = 100000007
    al = len(a)
    bl = len(b)
    if al>bl:
        return False

    t = pow(B, al, H)

    ah = 0
    bh = 0
    for i in range(al):
        ah = (ah * B + a[i]) % H
        bh = (bh * B + b[i]) % H

    for i in range(bl-al+1):
        if ah==bh:
            return True
        if i+al < bl:
            bh = (bh * B + b[i+al] - b[i] * t) % H

    return False

def resolve():
    T = SS()
    q = I()
    for _ in range(q):
        P = SS()
        if contain(P, T):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    resolve()
