import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    while True:
        n, m = LI()
        if n == m == 0:
            break
        else:
            ABC = [0] * n
            for i in range(3):
                tmp = LI_()
                for j in tmp[1:]:
                    ABC[j] = i

            dist = collections.defaultdict(lambda: INF)
            dist[tuple(ABC)] = 0
            que = collections.deque([ABC])
            while que:
                c = que.popleft()
                dist_c = dist[tuple(c)]

                # 終了条件
                if dist_c > m:
                    print(-1)
                    break
                if c.count(0) == n or c.count(2) == n:
                    print(dist_c)
                    break

                # 一番上のコップの大きさを探索
                top = [-1] * 3
                for i in range(n):
                    top[c[i]] = i
                    
                # コップ移動
                for i, j in ((0, 1), (1, 0), (1, 2), (2, 1)):
                    if top[i] > top[j]:
                        tmp = c[:]
                        tmp[top[i]] = j
                        if dist[tuple(tmp)] > dist_c + 1:
                            dist[tuple(tmp)] = dist_c + 1
                            que.append(tmp)

                # print(dist)
                # print(que)

if __name__ == '__main__':
    resolve()
