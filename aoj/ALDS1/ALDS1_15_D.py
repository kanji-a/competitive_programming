import sys, collections, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

class Node():
    left = None
    right = None

class HuffmanTree():
    root = None

def resolve():
    S = SS()

    cnt = collections.Counter(S)
    freq = list(cnt.values())
    ht = HuffmanTree()

    heapq.heapify(freq)
    while len(freq) >= 2:
        print(freq)
        l = heapq.heappop(freq)
        r = heapq.heappop(freq)
        heapq.heappush(freq, l+r)
        node = Node()


if __name__ == '__main__':
    resolve()
