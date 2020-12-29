import bisect, collections, copy, heapq, itertools, math, string, sys
from typing import NamedTuple, Optional, List, cast
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

class MFGraph:
    class Edge(NamedTuple):
        src: int
        dst: int
        cap: int
        flow: int

    class _Edge:
        def __init__(self, dst: int, cap: int) -> None:
            self.dst = dst
            self.cap = cap
            self.rev: Optional[MFGraph._Edge] = None

    def __init__(self, n: int) -> None:
        self._n = n
        self._g: List[List[MFGraph._Edge]] = [[] for _ in range(n)]
        self._edges: List[MFGraph._Edge] = []

    def add_edge(self, src: int, dst: int, cap: int) -> int:
        assert 0 <= src < self._n
        assert 0 <= dst < self._n
        assert 0 <= cap
        m = len(self._edges)
        e = MFGraph._Edge(dst, cap)
        re = MFGraph._Edge(src, 0)
        e.rev = re
        re.rev = e
        self._g[src].append(e)
        self._g[dst].append(re)
        self._edges.append(e)
        return m

    def get_edge(self, i: int) -> Edge:
        assert 0 <= i < len(self._edges)
        e = self._edges[i]
        re = cast(MFGraph._Edge, e.rev)
        return MFGraph.Edge(
            re.dst,
            e.dst,
            e.cap + re.cap,
            re.cap
        )

    def edges(self) -> List[Edge]:
        return [self.get_edge(i) for i in range(len(self._edges))]

    def change_edge(self, i: int, new_cap: int, new_flow: int) -> None:
        assert 0 <= i < len(self._edges)
        assert 0 <= new_flow <= new_cap
        e = self._edges[i]
        e.cap = new_cap - new_flow
        assert e.rev is not None
        e.rev.cap = new_flow

    def flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> int:
        assert 0 <= s < self._n
        assert 0 <= t < self._n
        assert s != t
        if flow_limit is None:
            flow_limit = cast(int, sum(e.cap for e in self._g[s]))

        current_edge = [0] * self._n
        level = [0] * self._n

        def fill(arr: List[int], value: int) -> None:
            for i in range(len(arr)):
                arr[i] = value

        def bfs() -> bool:
            fill(level, self._n)
            queue = []
            q_front = 0
            queue.append(s)
            level[s] = 0
            while q_front < len(queue):
                v = queue[q_front]
                q_front += 1
                next_level = level[v] + 1
                for e in self._g[v]:
                    if e.cap == 0 or level[e.dst] <= next_level:
                        continue
                    level[e.dst] = next_level
                    if e.dst == t:
                        return True
                    queue.append(e.dst)
            return False

        def dfs(lim: int) -> int:
            stack = []
            edge_stack: List[MFGraph._Edge] = []
            stack.append(t)
            while stack:
                v = stack[-1]
                if v == s:
                    flow = min(lim, min(e.cap for e in edge_stack))
                    for e in edge_stack:
                        e.cap -= flow
                        assert e.rev is not None
                        e.rev.cap += flow
                    return flow
                next_level = level[v] - 1
                while current_edge[v] < len(self._g[v]):
                    e = self._g[v][current_edge[v]]
                    re = cast(MFGraph._Edge, e.rev)
                    if level[e.dst] != next_level or re.cap == 0:
                        current_edge[v] += 1
                        continue
                    stack.append(e.dst)
                    edge_stack.append(re)
                    break
                else:
                    stack.pop()
                    if edge_stack:
                        edge_stack.pop()
                    level[v] = self._n
            return 0

        flow = 0
        while flow < flow_limit:
            if not bfs():
                break
            fill(current_edge, 0)
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                flow += f
                if f == 0:
                    break
        return flow

    def min_cut(self, s: int) -> List[bool]:
        visited = [False] * self._n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for e in self._g[v]:
                if e.cap > 0 and not visited[e.dst]:
                    visited[e.dst] = True
                    stack.append(e.dst)
        return visited

def resolve():
    N, M = LI()
    S = [SS() for _ in range(N)]
    d = ((1, 0), (0, 1), (-1, 0), (0, -1))

    g = MFGraph(N * M + 2)
    s = N * M
    t = N * M + 1

    # s→偶数マス、奇数マス→t
    for i, j in itertools.product(range(N), range(M)):
        if S[i][j] == '#':
            continue
        v = i * M + j
        if (i + j) % 2 == 0:
            g.add_edge(s, v, 1)
        else:
            g.add_edge(v, t, 1)

    # 偶数マス→奇数マス
    for i, j in itertools.product(range(N), range(M)):
        if (i + j) % 2 == 1 or S[i][j] == '#':
            continue
        v0 = i * M + j
        for dy, dx in d:
            ny = i + dy
            nx = j + dx
            if 0 <= ny < N and 0 <= nx < M and S[ny][nx] == '.':
                v1 = ny * M + nx
                g.add_edge(v0, v1, 1)

    # for i in g.edges():
    #     print(i)

    print(g.flow(s, t))

    # 解答の見た目作成
    ans = [list(i) for i in S]
    for i in g.edges():
        if i.src >= s or i.dst >= s or i.flow == 0:
            continue
        src_y, src_x = divmod(i.src, M)
        dst_y, dst_x = divmod(i.dst, M)
        if src_y == dst_y:
            ans[src_y][min(src_x, dst_x)] = '>'
            ans[src_y][max(src_x, dst_x)] = '<'
        else:
            ans[min(src_y, dst_y)][src_x] = 'v'
            ans[max(src_y, dst_y)][src_x] = '^'
    for i in ans:
        print(''.join(i))

if __name__ == '__main__':
    resolve()
