import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    C = [input() for _ in range(2)]

    ok = True
    for i in range(3):
        if C[0][i] != C[1][2-i]:
            ok = False
    if ok:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    resolve()