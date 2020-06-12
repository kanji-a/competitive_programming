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
    n = I()
    c = [I() for _ in range(n)]
    
    c_rl = [[], []]
    for i, e in enumerate(c):
        if not c_rl[0]:
            c_rl[0].append(e)
            c_rl[1].append(1)
        elif i%2==0:
            if e!=c_rl[0][-1]:
                c_rl[0].append(e)
                c_rl[1].append(1)
            else:
                c_rl[1][-1] += 1
        else:
            if e!=c_rl[-1]:
                c_rl[0][-1] = e
                c_rl[1][-1] += 1
                if len(c_rl[0])>=2 and c_rl[0][-2]==c_rl[0][-1]:
                    c_rl[0].pop()
                    last = c_rl[1].pop()
                    c_rl[1][-1] += last
            else:
                c_rl[1][-1] += 1
        # print(i, e, c_rl)
                    
    print(sum([c_rl[1][i] for i in range(len(c_rl[1])) if c_rl[0][i]==0]))

if __name__ == '__main__':
    resolve()