import sys, collections
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

    cnt = collections.Counter(A)
    A = list(set(A))
    A.sort()
    A_max = A[-1]
    divisible = [False] * (A_max + 1)

    for i in A:
        for j in range(2 * i, A_max+1, i):
            divisible[j] = True

    ans = 0
    for i in A:
        if not divisible[i] and cnt[i] == 1:
            ans += 1
        
    print(ans)

if __name__ == '__main__':
    resolve()