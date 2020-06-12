import sys
input = lambda: sys.stdin.readline().rstrip() 
import math

def resolve():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]

    ans = []
    def dfs(d, perm):
        if d==N:
            dist = 0
            for i in range(N-1):
                dist += ((xy[perm[i+1]][0]-xy[perm[i]][0])**2+(xy[perm[i+1]][1]-xy[perm[i]][1])**2)**0.5
            ans.append(dist)
        else:
            for i in range(N):
                if i not in perm:
                    dfs(d+1, perm+[i])

    dfs(0, [])
    print(sum(ans)/math.factorial(N))

if __name__ == '__main__':
    resolve()
