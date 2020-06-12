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
    c = LI()

    # [交互列の始点, 終点]
    c_rl = []
    c_rl.append([0, 1])
    for i in range(1, N):
        if c[i]!=c[i-1]:
            c_rl[-1][1] += 1
        else:
            c_rl.append([i, i+1])

    len_sum = sum([i[1]-i[0] for i in c_rl[:3]])
    ans = len_sum
    for i in range(len(c_rl)-3):
        len_sum = len_sum + (c_rl[i+3][1]-c_rl[i+3][0]) - (c_rl[i][1]-c_rl[i][0])
        # print(len_sum)
        ans = max(len_sum, ans)
    # print(c_rl)
    print(ans)

if __name__ == '__main__':
    resolve()
