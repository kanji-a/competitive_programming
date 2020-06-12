import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    N = int(input())
    s = [[0]*N for _ in range(N)]
    for _ in range(N*(N-1)//2):
        A, B, C, D = map(int, input().split())
        if C==D:
            s[A-1][B-1] = 1
            s[B-1][A-1] = 1
        elif C>D:
            s[A-1][B-1] = 3
            s[B-1][A-1] = 0
        elif C<D:
            s[A-1][B-1] = 0
            s[B-1][A-1] = 3

    total_score = [sum(i) for i in s]
    score_grade = {}
    found = set()
    for i, e in enumerate(sorted(total_score, reverse=True)):
        if not e in found:
            score_grade[e]=i+1
            found.add(e)

    for i in total_score:
        print(score_grade[i])

if __name__ == '__main__':
    resolve()
