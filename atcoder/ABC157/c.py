import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N, M = map(int, input().split())
    s = [0]*M
    c = [0]*M
    for i in range(M):
        s[i], c[i] = map(int, input().split())

    ans_int = ['-1']*N
    has_ans = True

    for s, c in zip(s, c):
        if ans_int[s-1] == '-1':
            ans_int[s-1] = str(c)
        elif ans_int[s-1] == str(c):
            pass
        else:
            has_ans = False

    for i, a in enumerate(ans_int):
        if a == '-1':
            if i == 0 and N > 1:
                ans_int[i] = '1'
            else:
                ans_int[i] = '0'

    if N != 1 and ans_int[0] == '0':
        has_ans = False

    if has_ans:
        print(''.join(ans_int))
    else:
        print('-1')

if __name__ == '__main__':
    resolve()
