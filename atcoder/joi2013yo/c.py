import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    name = input()
    board = [input() for _ in range(N)]

    ans = 0
    for i in board:
        has_name = False
        for j in range(1, (len(i)-1)//(len(name)-1)+1):
            for k in range(len(i)-(j*(len(name)-1)+1)+1):
                m = k
                is_ok = True
                for l in range(len(name)):
                    if i[m]!=name[l]:
                        is_ok = False
                    m += j
                if is_ok:
                    has_name = True
        if has_name:
            ans += 1

    print(ans)

if __name__ == '__main__':
    resolve()
