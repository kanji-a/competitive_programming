import sys
input = lambda: sys.stdin.readline().rstrip() 

def resolve():
    S = input()
    
    def rec(s):
        len_s = len(s)
        # 最初の一番内側の()の中身を処理する
        stk = []
        if '(' not in s:
            return s
        i_f = -1
        i_b = -1
        for i in range(len_s):
            if s[i] == '(':
                stk.append(i)
            if s[i] == ')':
                i_f = stk.pop()
                i_b = i
                break
        res = rec(s[:i_f] + s[i_f+1:i_b] + s[i_b-1:i_f:-1] + s[i_b+1:])
        return res

    ans = rec(S)
    print(ans)

if __name__ == '__main__':
    resolve()
