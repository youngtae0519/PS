import sys
input = sys.stdin.readline

def dfs(N, arr):
    if N > 1:
        for i in range(3):
            arr.append(cal[i])
            dfs(N - 1, arr)
            arr.pop()
    elif N == 1:
        ans = []
        tmp = []

        for i in range(1, len(arr) + 1):
            ans.append(str(i))
            ans.append(arr[i - 1])
            tmp.append(str(i))
            if arr[i - 1] != ' ':
                tmp.append(arr[i - 1])

        ans.append(str(len(arr) + 1))
        tmp.append(str(len(arr) + 1)) 

        if eval(''.join(tmp)) == 0:
            print(''.join(ans))
        


T = int(input())
cal = [' ', '+', '-']

for _ in range(T):
    N = int(input())

    dfs(N, [])

    if _ != T - 1:
        print()