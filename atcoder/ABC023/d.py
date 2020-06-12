import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    HS = [list(map(int, input().split())) for _ in range(N)]

    # for i in HS:
    #     print([i[0]+i[1]*j for j in range(N)])
    
    # 高度xまでで全部割れるか
    def can_break_all(x):
        # print(sorted([(x-hs[0])//hs[1] for hs in HS]))
        is_ok = True
        for i, e in enumerate(sorted([(x-h)//s for h, s in HS])):
            if i>e:
                is_ok = False
        return is_ok

    ng = 0
    ok = max([h+s*N for h, s in HS])
    while abs(ok-ng)>1:
        m = (ng+ok)//2
        if can_break_all(m):
            ok = m
        else:
            ng = m
    print(ok)

if __name__ == '__main__':
    resolve()
