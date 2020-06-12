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

    k = int((2*N)**0.5)+1
    if k*(k-1)//2==N:
        ans = [[] for _ in range(k)]
        num = 1
        # 層
        for i in range(k-1):
            for j in range(i+1):
                ans[j].append(num)
                ans[i+1].append(num)
                num += 1
        print('Yes')
        print(k)
        for i in ans:
            print(k-1, *i)
    else:
        print('No')

# N=6のとき
#     (1, 2, 4),
#     (1, 3, 5),
#     (2, 3, 6),
#     (4, 5, 6)

if __name__ == '__main__':
    resolve()