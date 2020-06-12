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
    con = [[[INF, 0] for _ in range(N)] for _ in range(N)]
    for i in range(M):
        stdtime = LI()
        con[stdtime[0]-1][stdtime[1]-1] = [stdtime[2], stdtime[3]]
        con[stdtime[1]-1][stdtime[0]-1] = [stdtime[2], stdtime[3]]

    dp_cost = [[INF]*N for _ in range(2**N)]
    dp_count = [[0]*N for _ in range(2**N)]
    dp_cost[1][0] = 0
    dp_count[1][0] = 1

    for i in range(1, N):
        for selected in itertools.combinations(range(N), i+1):
            v_set = sum([1<<j for j in selected])
            for k in range(N):
                if v_set>>k & 1:
                    min_time = INF
                    min_time_count = 0
                    for l in range(N):
                        next_time_count = [dp_cost[v_set&~(1<<k)][l] + con[l][k][0], dp_count[v_set&~(1<<k)][l]]
                        if v_set>>l & 1 and l!=k and next_time_count[0]<=con[l][k][1]:
                            if min_time>next_time_count[0]:
                                min_time = next_time_count[0]
                                min_time_count = next_time_count[1]
                            elif min_time==next_time_count[0]:
                                min_time_count += next_time_count[1]
                    dp_cost[v_set][k] = min_time
                    dp_count[v_set][k] = min_time_count
    
    # for i in range(2**N):
    #     print(bin(i), dp[i])
    is_impossible = False
    return_time_count = [[dp_cost[-1][i]+con[i][0][0], dp_count[-1][i]] for i in range(N) if dp_cost[-1][i]+con[i][0][0]<=con[i][0][1]]
    if len(return_time_count)==0:
        is_impossible = True
    if not is_impossible:
        min_time = min([i[0] for i in return_time_count])
        if min_time >= INF:
            is_impossible = True
    if is_impossible:
        print('IMPOSSIBLE')
    else:
        min_time_count = sum([i[1] for i in return_time_count if i[0]==min_time])
        print(min_time, min_time_count)

if __name__ == '__main__':
    resolve()