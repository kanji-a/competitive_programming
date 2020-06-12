import sys
input = lambda: sys.stdin.readline().rstrip() 
import heapq

def resolve():
    N = int(input())
    tasks = [[] for _ in range(N)]
    for i in range(N):
        A, B = map(int, input().split())
        tasks[A-1].append(-B)
    hq = []
    heapq.heapify(hq)

    ans = [0]*N
    for i in range(N):
        for j in tasks[i]:
            heapq.heappush(hq, j)
        if i==0:
            ans[i] = -1*heapq.heappop(hq)
        else:
            ans[i] = ans[i-1]-heapq.heappop(hq)

    for i in ans:
        print(i)

if __name__ == '__main__':
    resolve()
