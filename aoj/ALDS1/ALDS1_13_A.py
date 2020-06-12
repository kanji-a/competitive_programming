import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    k = int(input())
    rc = [list(map(int, input().split())) for _ in range(k)]
 
    def dfs(d, perm):
        if d==8:
            ok = True
            for i in rc:
                if perm[i[0]]!=i[1]:
                    ok = False
            if ok:
                okok = True
                for j in range(7):
                    for k in range(j+1, 8):
                        if j-perm[j]==k-perm[k] or j+perm[j]==k+perm[k]:
                            okok = False
                if okok:
                    for j in range(8):
                        pos = perm[j]
                        print('.'*pos+'Q'+'.'*(7-pos))
            return perm
        else:
            for i in range(8):
                if i not in perm:
                    dfs(d+1, perm+[i])
    dfs(0, [])

if __name__ == '__main__':
    resolve()