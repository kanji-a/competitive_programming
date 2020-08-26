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

def split_list(a):
    ret = []
    tmp = []
    l = len(a)
    for i in range(l):
        tmp.append(a[i])
        if i < l - 1 and a[i] < a[i+1] or i == l - 1:
            ret.append(tmp)
            tmp = []
    return ret

def resolve():
    N = I()
    H = LI()

    l = split_list(H)
    ans = max([len(i) for i in l]) - 1
    print(ans)

if __name__ == '__main__':
    resolve()
