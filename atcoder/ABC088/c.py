import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    c = [list(map(int, input().split())) for _ in range(3)]

    absum = []

    def dfs(depth, perm, s):
        if depth==3:
            absum.append(s)
        else:
            for i in range(3):
                if not i in perm:
                    dfs(depth+1, perm+[i], s+c[depth][i])

    dfs(0, [], 0)

    if len(set(absum))==1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()
