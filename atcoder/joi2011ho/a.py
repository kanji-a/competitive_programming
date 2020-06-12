import sys
import numpy as np
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
    M, N = LI()
    K = I()
    planet = [S() for _ in range(M)]

    # cumsumが半開区間じゃないのの対策
    cnt_j = np.zeros((M+1, N+1))
    cnt_o = np.zeros((M+1, N+1))
    cnt_i = np.zeros((M+1, N+1))
    for i in range(M):
        for j in range(N):
            if planet[i][j]=='J':
                cnt_j[i+1][j+1] = 1
            elif planet[i][j]=='O':
                cnt_o[i+1][j+1] = 1
            elif planet[i][j]=='I':
                cnt_i[i+1][j+1] = 1
    acc_j = np.cumsum(np.cumsum(cnt_j, axis=1), axis=0)
    acc_o = np.cumsum(np.cumsum(cnt_o, axis=1), axis=0)
    acc_i = np.cumsum(np.cumsum(cnt_i, axis=1), axis=0)

    for i in range(K):
        a, b, c, d = LI_()
        ans_j = acc_j[c+1][d+1] - acc_j[c+1][b] - acc_j[a][d+1] + acc_j[a][b]
        ans_o = acc_o[c+1][d+1] - acc_o[c+1][b] - acc_o[a][d+1] + acc_o[a][b]
        ans_i = (c+1-a)*(d+1-b) - ans_j - ans_o
        print(int(ans_j), int(ans_o), int(ans_i))

if __name__ == '__main__':
    resolve()