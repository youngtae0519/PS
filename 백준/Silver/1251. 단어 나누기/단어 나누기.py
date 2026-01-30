import sys

input = sys.stdin.readline

S = input().rstrip()
ans = []
for i in range(len(S) - 2):
    for j in range(i + 1, len(S) - 1):
        tmp = ''
        for k in range(i, -1, -1):
            tmp += S[k]
        for k in range(j, i, -1):
            tmp += S[k]
        for k in range(len(S) - 1, j, -1):
            tmp += S[k]
        ans.append(tmp)

ans.sort()
print(ans[0])