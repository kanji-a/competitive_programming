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
    T = list(S())

    L = len(T)
    # print(T)
    for i in range(L):
        if T[i]=='?':
            T[i] = 'D'

    print(''.join(T))

    # if T[-1]=='?':
    #     T[-1] = 'D'
    # for i in range(L-1):
    #     print(L-1-i)
    #     c_first = T[L-2-i]
    #     c_second = T[L-1-i]
    #     print(c_first, c_second)
    #     if c_second=='P':
    #         T[L-1-i] = 'D'
    #     else c_second=='D':


if __name__ == '__main__':
    resolve()