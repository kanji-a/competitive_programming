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
    X = I()

    i = 0
    while i**5<X:
        i += 1
    
    B = -(i-1)
    while True:
        A = int((B**5+X)**0.2)
        if A**5==B**5+X:
            break
        B += 1

    print(A, B)

if __name__ == '__main__':
    resolve()