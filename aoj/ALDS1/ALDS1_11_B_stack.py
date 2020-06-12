import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    n = int(input())
    ukv = [list(map(int, input().split())) for _ in range(n)]

    d = [-1]*n
    f = [-1]*n
    stk = []
    status = [0]*n

    t = 1
    for i in range(n):
        if status[i]==0:
            stk.append(i)
            while len(stk)>0:
                a = stk[-1]
                if status[a]==0:
                    d[a] = t
                    t += 1
                    status[a] = 1
                elif status[a]==1:
                    stk.pop()
                    f[a] = t
                    t += 1
                    status[a] = 2
                else:
                    stk.pop()
                for i in reversed(ukv[a][2:]):
                    if status[i-1]==0:
                        stk.append(i-1) 

    for i in range(n):
        print(i+1, d[i], f[i])

if __name__ == '__main__':
    resolve()