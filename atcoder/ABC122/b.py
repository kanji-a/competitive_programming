import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()
    acgt = ('A', 'C', 'G', 'T')
    ans = 0

    for l in range(len(S)):
        for r in range(l+1, len(S)+1):
            # print(l, r, S[l:r])
            if S[r-1] not in acgt:
                ans = max(r-1-l, ans)
                break
            if r==len(S):
                ans = max(len(S)-l, ans)
 
    print(ans)

if __name__ == '__main__':
    resolve()
