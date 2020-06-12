import sys, itertools
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
    N, M = LI()
    # arena = [0, 5, 1, 4, 2, 3]
    arena = []
    # for i in range(M):
    #     arena.append([i, 2*M-1-i])

    # for i in range(N):
    #     print(arena)
    #     arena= [[(i[0]+1)%N, (i[1]+1)%N] for i in arena]

    n = 8
    m = 3

    s = set()
    for i in itertools.permutations(range(n), n):
        tmp = []
        for j in range(m):
            tmp.append((i[j*2]-i[j*2+1])%n)
        if len(set(tmp))==m:
            s.add(str(sorted(tmp)))
            # print(i, tmp)
    print(s)

if __name__ == '__main__':
    resolve()
